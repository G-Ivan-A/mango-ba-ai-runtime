"""Checks that the published KB navigation stays complete after re-extraction."""

import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
KB = ROOT / "docs/kb"
ONE_READ_LIMIT = 32768  # RFC-RT-001, РТ-7: the reference size of one file read in a chat
TOC_HEADER = "section\ttitle\tfile"


def toc_rows(document):
    """Parse a TOC the way USAGE.md describes it: plain lines of tab-separated fields."""
    lines = (ROOT / document["sections_toc"]).read_bytes().decode("utf-8").split("\n")
    return lines[0], [line.split("\t") for line in lines[1:-1]]


class KnowledgeBaseNavigationTest(unittest.TestCase):
    def test_generated_maps_are_current(self):
        result = subprocess.run(
            ["python", "docs/kb/build_map.py", "--check"],
            cwd=ROOT,
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(result.returncode, 0, result.stderr)

    def test_map_covers_every_indexed_section_and_product_class(self):
        root_map = json.loads((KB / "MAP.json").read_text())
        self.assertEqual(root_map["taxonomy_ref"], "taxonomy/products.yaml#classes")
        taxonomy = (ROOT / "taxonomy/products.yaml").read_text()
        class_ids = set(re.findall(r"\{id: ([a-z-]+), name:", taxonomy))
        listed_indexes = set()
        listed_sections = set()

        for document in root_map["documents"]:
            self.assertTrue(set(document["product_ids"]) <= class_ids)
            index = ROOT / document["index"]
            self.assertTrue(index.is_file(), index)
            self.assertIn("product_ids:", index.read_text())
            self.assertIn("product_taxonomy_ref: taxonomy/products.yaml#classes", index.read_text())
            listed_indexes.add(index)

            section_map = json.loads((ROOT / document["sections_map"]).read_text())
            self.assertEqual(section_map["document_id"], document["id"])
            self.assertEqual(section_map["product_ids"], document["product_ids"])
            self.assertEqual(document["section_count"], len(section_map["sections"]))
            for section in section_map["sections"]:
                path = ROOT / section["path"]
                self.assertTrue(path.is_file(), path)
                self.assertIn("title", section)
                self.assertIn("hint", section)
                listed_sections.add(path)

        actual_sections = set(KB.glob("**/sections/*.md"))
        actual_indexes = {path.parent.parent / "index.md" for path in actual_sections}
        self.assertEqual(listed_sections, actual_sections)
        self.assertEqual(listed_indexes, actual_indexes)

    def test_representative_questions_have_exact_section_targets(self):
        root_map = json.loads((KB / "MAP.json").read_text())
        by_id = {item["id"]: item for item in root_map["documents"]}
        for doc_id, phrase in (
            ("vpbx-api", 'О параметре "sign"'),
            ("speech-analytics--user-guide", "Настройки распознавания записей"),
            ("integration-amocrm", "Сопоставление сотрудников"),
            # The last section of the manual: RUN-0083 read its map only partly and missed it.
            ("mango-lk-manual", "Роли и права доступа ЛК ВАТС"),
        ):
            document = by_id[doc_id]
            _, rows = toc_rows(document)
            matches = [row for row in rows if phrase.casefold() in row[1].casefold()]
            self.assertTrue(matches, (doc_id, phrase))
            sections = ROOT / Path(document["index"]).parent / "sections"
            self.assertTrue(all((sections / row[2]).is_file() for row in matches))

    def test_every_document_has_a_toc_matching_its_map_within_one_read(self):
        documents = json.loads((KB / "MAP.json").read_text())["documents"]
        self.assertEqual(
            {ROOT / document["sections_toc"] for document in documents},
            set((KB / "maps").glob("*.toc.tsv")),
        )
        for document in documents:
            with self.subTest(document=document["id"]):
                self.assertEqual(document["sections_toc"], f"docs/kb/maps/{document['id']}.toc.tsv")
                toc = ROOT / document["sections_toc"]
                self.assertLessEqual(toc.stat().st_size, ONE_READ_LIMIT)

                content = toc.read_bytes().decode("utf-8")
                self.assertNotIn("\r", content)
                self.assertTrue(content.endswith("\n"))
                self.assertFalse(content.endswith("\n\n"))

                header, rows = toc_rows(document)
                self.assertEqual(header, TOC_HEADER)
                sections = json.loads((ROOT / document["sections_map"]).read_text())["sections"]
                self.assertEqual(
                    rows,
                    [
                        [
                            section["section"].replace("\t", " "),
                            section["title"].replace("\t", " "),
                            Path(section["path"]).name,
                        ]
                        for section in sections
                    ],
                )
                # The way USAGE.md resolves a file gives the exact path of the map.
                directory = Path(document["index"]).parent / "sections"
                self.assertEqual(
                    [(directory / row[2]).as_posix() for row in rows],
                    [section["path"] for section in sections],
                )

    def test_root_map_stays_within_one_read(self):
        # The TOC does not help if the file that leads to it cannot be read at once.
        self.assertLessEqual((KB / "MAP.json").stat().st_size, ONE_READ_LIMIT)

    def test_navigation_opens_the_toc_before_the_map(self):
        navigation = json.loads((KB / "MAP.json").read_text())["navigation"]
        self.assertIn("sections_toc", navigation["select_document"])
        self.assertNotIn("sections_map", navigation["select_document"])
        select_section = navigation["select_section"]
        self.assertLess(select_section.index("sections_toc"), select_section.index("title"))
        self.assertLess(select_section.index("title"), select_section.index("sections_map"))
        self.assertIn("sections_toc", navigation["retrieval_if_insufficient"][0])

        step_2 = re.search(r"^2\. .*?(?=^3\. )", (KB / "USAGE.md").read_text(), re.M | re.S).group(0)
        self.assertLess(step_2.index("sections_toc"), step_2.index("`title`"))
        self.assertLess(step_2.index("`title`"), step_2.index("sections_map"))

    def test_line_range_from_usage_contains_the_map_record(self):
        # USAGE.md, step 2: without search a record is read by its TOC position.
        for path in (KB / "maps").glob("*.json"):
            lines = path.read_text().split("\n")
            sections = json.loads("\n".join(lines))["sections"]
            for number, section in enumerate(sections, start=1):
                excerpt = "\n".join(lines[9 * number - 2 : 9 * number + 8])
                start = excerpt.index("    {\n")
                end = excerpt.index("    }", start) + len("    }")
                self.assertEqual(json.loads(excerpt[start:end]), section, (path.name, number))

    def test_remaining_image_links_resolve(self):
        image_link = re.compile(r"!\[[^\]\n]*\]\((\.\./images/[^)\n]+)\)")
        referenced = []
        for section in KB.glob("**/sections/*.md"):
            for target in image_link.findall(section.read_text()):
                image = (section.parent / target).resolve()
                self.assertTrue(image.is_file(), (section, target))
                referenced.append(image)
        images = {path.resolve() for path in KB.glob("**/images/*") if path.is_file()}
        # Pixel-identical illustrations share one file (issue #11), so a file may
        # be referenced several times; every file must still be referenced.
        self.assertEqual(set(referenced), images)


class BuildMapTest(unittest.TestCase):
    """Runs the generator on a one-document copy of the KB: the working tree stays intact."""

    DOCUMENT = "mtalker/quick-start"
    DOCUMENT_ID = "mtalker--quick-start"

    def setUp(self):
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name)
        for relative in ("docs/kb/build_map.py", "taxonomy/products.yaml", f"docs/kb/{self.DOCUMENT}/index.md"):
            target = self.root / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy(ROOT / relative, target)
        shutil.copytree(KB / self.DOCUMENT / "sections", self.root / "docs/kb" / self.DOCUMENT / "sections")
        self.maps = self.root / "docs/kb/maps"
        self.toc = self.maps / f"{self.DOCUMENT_ID}.toc.tsv"
        self.assertEqual(self.generate().returncode, 0)

    def generate(self, *args, env=None):
        return subprocess.run(
            [sys.executable, str(self.root / "docs/kb/build_map.py"), *args],
            capture_output=True,
            text=True,
            check=False,
            env=env,
        )

    def assert_check_reports(self, name):
        result = self.generate("--check")
        self.assertEqual(result.returncode, 1, result.stdout)
        self.assertIn(f"docs/kb/maps/{name}", result.stderr)

    def first_title(self):
        map_path = self.maps / f"{self.DOCUMENT_ID}.json"
        return json.loads(map_path.read_text(encoding="utf-8"))["sections"][0]["title"]

    def rename_first_section(self, title):
        index = self.root / "docs/kb" / self.DOCUMENT / "index.md"
        text = index.read_text(encoding="utf-8")
        cell = f"| {self.first_title()} |"
        self.assertIn(cell, text)
        index.write_text(text.replace(cell, f"| {title} |", 1), encoding="utf-8")

    def test_fresh_build_passes_check(self):
        result = self.generate("--check")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("1 document maps, 1 section TOCs and MAP.json", result.stdout)

    def test_check_reports_edited_toc(self):
        self.toc.write_bytes(self.toc.read_bytes() + b"9\tExtra\t99-extra.md\n")
        self.assert_check_reports(self.toc.name)

    def test_check_reports_toc_with_windows_line_endings(self):
        self.toc.write_bytes(self.toc.read_bytes().replace(b"\n", b"\r\n"))
        self.assert_check_reports(self.toc.name)

    def test_check_reports_missing_toc(self):
        self.toc.unlink()
        self.assert_check_reports(self.toc.name)

    def test_check_reports_extra_toc_like_extra_map(self):
        (self.maps / "removed-document.toc.tsv").write_text("section\ttitle\tfile\n", encoding="utf-8")
        self.assert_check_reports("removed-document.toc.tsv")
        (self.maps / "removed-document.toc.tsv").unlink()
        (self.maps / "removed-document.json").write_text("{}\n", encoding="utf-8")
        self.assert_check_reports("removed-document.json")

    def test_check_reports_toc_after_section_rename(self):
        self.rename_first_section("Новое название")
        self.assert_check_reports(self.toc.name)
        self.assertEqual(self.generate().returncode, 0)
        self.assertEqual(self.generate("--check").returncode, 0)
        self.assertEqual(self.toc.read_text(encoding="utf-8").split("\n")[1].split("\t")[1], "Новое название")

    def test_tab_in_title_becomes_space_and_keeps_one_line_per_section(self):
        before = self.toc.read_text(encoding="utf-8").split("\n")
        self.rename_first_section("Быстрый\tстарт")
        self.assertEqual(self.generate().returncode, 0)
        self.assertEqual(self.first_title(), "Быстрый\tстарт")  # the map keeps the source value
        after = self.toc.read_text(encoding="utf-8").split("\n")
        self.assertEqual(len(after), len(before))
        self.assertEqual(after[1].split("\t")[1], "Быстрый старт")
        self.assertTrue(all(line.count("\t") == 2 for line in after[:-1]))

    def test_outputs_are_utf8_under_a_non_utf8_locale(self):
        env = {**os.environ, "LC_ALL": "C", "PYTHONCOERCECLOCALE": "0", "PYTHONUTF8": "0"}
        expected = self.toc.read_bytes()
        self.assertEqual(self.generate("--check", env=env).returncode, 0)
        self.assertEqual(self.generate(env=env).returncode, 0)
        self.assertEqual(self.toc.read_bytes(), expected)


if __name__ == "__main__":
    unittest.main()
