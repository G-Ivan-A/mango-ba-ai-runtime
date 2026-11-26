"""OpenCode initialisation smoke for this repository (RFC-RT-002, Э4; BL-192).

Checks, without a model run of the route, that an OpenCode client started in
this repository

1. (V1) lists exactly the 11 route skills in `opencode debug skill`, each
   found in the mirror .agents/skills/<name>/SKILL.md;
2. (V1, V2) sends AGENTS.md to the model in full as project instructions and
   offers it the 11 skills with the descriptions of skills/<name>.md;
3. (control) offers none of them in a copy of AGENTS.md and skills/ without
   the mirror: discovery comes from the mirror, not from the flat layout.

Step 2 needs a model request. The script starts a local mock of an
OpenAI-compatible endpoint, records the request and answers «ok»: no real model
is called and no key is used. OpenCode runs with an isolated HOME and XDG
directories, so the user's global config, skills and sessions are not read.
The provider package @ai-sdk/openai-compatible is installed by OpenCode itself
on first use (network access to the npm registry).

    npm install --prefix /tmp/oc opencode-ai@1.19.6        # line V1
    npm install --prefix /tmp/oc2 @opencode/cli@2.4.2      # line V2
    python3 tests/opencode_smoke.py --opencode /tmp/oc/node_modules/.bin/opencode

The OpenCode version is chosen by the caller; pinning it is BL-132 of
G-Ivan-A/mango_ba_prompts. Exit code 0 means every check passed.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
import tempfile
import threading
import time
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tests"))

import agent_context_audit as audit  # noqa: E402

PROMPT = "перечисли навыки"
AGENTS_TITLE = "# AGENTS.md: системный промпт исполнения маршрута RG-BCREQ-v1"


def route_skills() -> dict[str, str]:
    """Skill name -> normalised description from skills/<name>.md."""
    skills = {}
    for path in sorted((ROOT / "skills").glob("*.md")):
        text = path.read_text(encoding="utf-8")
        skills[audit.frontmatter(text)["name"]] = " ".join(audit.block_value(text, "description").split())
    return skills


class MockModel(BaseHTTPRequestHandler):
    """Minimal OpenAI-compatible chat completions endpoint that records requests."""

    requests: list[dict] = []

    def log_message(self, *args):
        pass

    def _send(self, status: int, ctype: str, body: bytes):
        self.send_response(status)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        self._send(200, "application/json", json.dumps({"object": "list", "data": [{"id": "m", "object": "model"}]}).encode())

    def do_POST(self):
        raw = self.rfile.read(int(self.headers.get("Content-Length", 0)))
        request = json.loads(raw or b"{}")
        MockModel.requests.append(request)
        base = {"id": "smoke", "created": int(time.time()), "model": "m"}
        usage = {"prompt_tokens": 1, "completion_tokens": 1, "total_tokens": 2}
        if request.get("stream"):
            chunks = [
                {**base, "object": "chat.completion.chunk",
                 "choices": [{"index": 0, "delta": {"role": "assistant", "content": "ok"}, "finish_reason": None}]},
                {**base, "object": "chat.completion.chunk",
                 "choices": [{"index": 0, "delta": {}, "finish_reason": "stop"}]},
                {**base, "object": "chat.completion.chunk", "choices": [], "usage": usage},
            ]
            body = b"".join(b"data: " + json.dumps(c).encode() + b"\n\n" for c in chunks) + b"data: [DONE]\n\n"
            self._send(200, "text/event-stream", body)
        else:
            self._send(200, "application/json", json.dumps({
                **base, "object": "chat.completion", "usage": usage,
                "choices": [{"index": 0, "message": {"role": "assistant", "content": "ok"}, "finish_reason": "stop"}],
            }).encode())


def isolated_env(home: Path, port: int) -> dict[str, str]:
    config = home / ".config" / "opencode"
    config.mkdir(parents=True)
    (config / "opencode.json").write_text(json.dumps({
        "$schema": "https://opencode.ai/config.json",
        "autoupdate": False,
        "share": "disabled",
        "provider": {"smoke": {
            "npm": "@ai-sdk/openai-compatible",
            "name": "smoke",
            "options": {"baseURL": f"http://127.0.0.1:{port}/v1", "apiKey": "smoke"},
            "models": {"m": {"name": "m"}},
        }},
        "model": "smoke/m",
        "small_model": "smoke/m",
    }, indent=2), encoding="utf-8")
    env = {k: v for k, v in os.environ.items() if not k.startswith(("OPENCODE", "XDG_"))}
    env.update({
        "HOME": str(home),
        "XDG_CONFIG_HOME": str(home / ".config"),
        "XDG_DATA_HOME": str(home / ".local" / "share"),
        "XDG_CACHE_HOME": str(home / ".cache"),
        "XDG_STATE_HOME": str(home / ".local" / "state"),
        "OPENCODE_DISABLE_AUTOUPDATE": "1",
    })
    return env


def text_of(request: dict) -> str:
    return json.dumps(request, ensure_ascii=False)


def system_of(request: dict) -> str:
    parts = []
    for message in request.get("messages", []):
        if message.get("role") == "system":
            content = message.get("content")
            parts.append(content if isinstance(content, str) else json.dumps(content, ensure_ascii=False))
    return "\n".join(parts)


SKILL_BLOCK = re.compile(r"<skill>(.*?)</skill>", re.S)


def offered_skills(request: dict) -> dict[str, tuple[str, str]]:
    """Skills the client offers the model: name -> (description, location or "")."""
    text = ""
    for message in request.get("messages", []):
        content = message.get("content")
        text += (content if isinstance(content, str) else json.dumps(content, ensure_ascii=False)) + "\n"
    for tool in request.get("tools", []):
        text += str(tool.get("function", {}).get("description", "")) + "\n"
    skills = {}
    for block in SKILL_BLOCK.findall(text):
        field = lambda tag: (re.search(rf"<{tag}>(.*?)</{tag}>", block, re.S) or [None, ""])[1]
        # V2 names a skill by <id> (and a display <name>); V1 only by <name>.
        key = field("id").strip() or field("name").strip()
        skills[key] = (" ".join(field("description").split()), field("location").strip())
    return skills


def run_client(opencode: str, major: int, cwd: Path, env: dict, timeout: int) -> tuple[subprocess.CompletedProcess, dict]:
    """One prompt through the client; returns the process and the recorded main request."""
    MockModel.requests.clear()
    if major >= 2:
        cmd = [opencode, "run", "--standalone", "--archived", "-m", "smoke/m", PROMPT]
    else:
        cmd = [opencode, "run", "--pure", "-m", "smoke/m", PROMPT]
    # V2 takes the project directory from $PWD, not from the process cwd.
    proc = subprocess.run(cmd, cwd=cwd, env={**env, "PWD": str(cwd)}, capture_output=True, text=True,
                          stdin=subprocess.DEVNULL, timeout=timeout)
    main = [r for r in MockModel.requests if PROMPT in text_of(r) and r.get("tools")]
    return proc, (main[-1] if main else {})


def control_project(base: Path) -> Path:
    """AGENTS.md and the flat skills/ without the mirror: what clients saw before Э1."""
    project = base / "control"
    (project / "skills").mkdir(parents=True)
    (project / "AGENTS.md").write_bytes((ROOT / "AGENTS.md").read_bytes())
    for path in (ROOT / "skills").glob("*.md"):
        (project / "skills" / path.name).write_bytes(path.read_bytes())
    subprocess.run(["git", "init", "-q", str(project)], check=True)
    return project


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description="OpenCode initialisation smoke (RFC-RT-002, Э4)")
    parser.add_argument("--opencode", required=True, help="path to the opencode executable (V1 or V2)")
    parser.add_argument("--timeout", type=int, default=240, help="seconds per opencode call")
    parser.add_argument("--no-control", action="store_true", help="skip the control run without the mirror")
    args = parser.parse_args(argv)

    want = route_skills()
    failures = 0

    def check(ok: bool, label: str, detail: str = "") -> None:
        nonlocal failures
        print(f"{'ok' if ok else 'not ok'} - {label}" + (f": {detail}" if detail and not ok else ""))
        failures += 0 if ok else 1

    version = subprocess.run([args.opencode, "--version"], capture_output=True, text=True, timeout=args.timeout)
    version_text = (version.stdout or version.stderr).strip()
    found = re.search(r"(\d+)\.\d+\.\d+", version_text)
    major = int(found[1]) if found else 1
    print(f"# opencode {version_text} (line V{major})")

    server = ThreadingHTTPServer(("127.0.0.1", 0), MockModel)
    threading.Thread(target=server.serve_forever, daemon=True).start()
    home = Path(tempfile.mkdtemp(prefix="opencode-smoke-"))
    env = isolated_env(home, server.server_address[1])
    try:
        # 1. V1 only: the client's own skill list, with file locations.
        if major < 2:
            listed = subprocess.run([args.opencode, "debug", "skill", "--pure"], cwd=ROOT, env=env,
                                    capture_output=True, text=True, timeout=args.timeout)
            try:
                entries = json.loads(listed.stdout)
            except json.JSONDecodeError:
                entries = None
            check(listed.returncode == 0 and isinstance(entries, list), "opencode debug skill returns a list",
                  (listed.stderr or listed.stdout)[-500:])
            project = {e.get("name"): str(e.get("location", "")) for e in entries or []
                       if str(e.get("location", "")).startswith(str(ROOT))}
            check(set(project) == set(want), f"debug skill lists the {len(want)} route skills", f"{sorted(project)}")
            for name in want:
                location = project.get(name, "")
                rel = Path(location).relative_to(ROOT).as_posix() if location else ""
                check(rel == f".agents/skills/{name}/SKILL.md", f"debug skill finds {name} in the mirror", rel)

        # 2. AGENTS.md reaches the model as instructions, the 11 skills are offered.
        proc, request = run_client(args.opencode, major, ROOT, env, args.timeout)
        check(proc.returncode == 0 and bool(request), "opencode run reaches the mock model",
              (proc.stderr or proc.stdout)[-500:])
        system = system_of(request)
        agents = (ROOT / "AGENTS.md").read_text(encoding="utf-8")
        check(f"Instructions from: {ROOT / 'AGENTS.md'}" in system, "AGENTS.md is loaded as project instructions")
        body = agents.split("\n---\n", 1)[-1].strip()
        check(AGENTS_TITLE in system and body in system, "AGENTS.md reaches the model in full",
              f"{len(system)} bytes of system prompt")
        offered = offered_skills(request)
        for name, description in want.items():
            got_description, location = offered.get(name, ("", ""))
            check(name in offered, f"skill {name} is offered to the model")
            check(got_description == description, f"skill {name} keeps its description")
            if location:
                rel = Path(location).relative_to(ROOT).as_posix() if location.startswith(str(ROOT)) else location
                check(rel == f".agents/skills/{name}/SKILL.md", f"skill {name} is read from the mirror", rel)
        foreign = [n for n, (_, loc) in offered.items() if n not in want and loc.startswith(str(ROOT))]
        check(not foreign, "no other project skills are offered", f"{foreign}")

        # 3. Control: without the mirror the client offers none of the route skills.
        if not args.no_control:
            _, request = run_client(args.opencode, major, control_project(home), env, args.timeout)
            seen = sorted(set(want) & set(offered_skills(request)))
            check(bool(request) and not seen, "control without the mirror offers no route skills", f"{seen}")
    finally:
        server.shutdown()
        subprocess.run(["rm", "-rf", str(home)], check=False)

    print(f"# {'passed' if failures == 0 else f'failed: {failures} check(s)'}")
    return 0 if failures == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
