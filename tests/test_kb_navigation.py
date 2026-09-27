"""Checks that the published KB navigation stays complete after re-extraction."""

import json
import re
import subprocess
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
KB = ROOT / "docs/kb"


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
            meta = json.loads((index.parent / "meta.json").read_text())
            self.assertEqual(meta["image_count"], len(list((index.parent / "images").glob("*"))))
            self.assertGreaterEqual(meta["image_count_extracted"], meta["image_count"])
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
        ):
            section_map = json.loads((ROOT / by_id[doc_id]["sections_map"]).read_text())
            matches = [s for s in section_map["sections"] if phrase.casefold() in s["title"].casefold()]
            self.assertTrue(matches, (doc_id, phrase))
            self.assertTrue(all((ROOT / s["path"]).is_file() for s in matches))

    def test_remaining_image_links_resolve(self):
        image_link = re.compile(r"!\[[^\]\n]*\]\((\.\./images/[^)\n]+)\)")
        referenced = []
        for section in KB.glob("**/sections/*.md"):
            for target in image_link.findall(section.read_text()):
                image = (section.parent / target).resolve()
                self.assertTrue(image.is_file(), (section, target))
                referenced.append(image)
        images = {path.resolve() for path in KB.glob("**/images/*") if path.is_file()}
        self.assertEqual(len(referenced), len(images))
        self.assertEqual(set(referenced), images)


if __name__ == "__main__":
    unittest.main()
