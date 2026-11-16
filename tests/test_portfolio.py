"""Unit tests for offline Markdown/SVG validation."""
from pathlib import Path
import tempfile
import unittest

from scripts.check_portfolio import relative_targets, validate_links, validate_svg


class PortfolioCheckTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        (self.root / "assets").mkdir()
        (self.root / "README.md").write_text("Example", encoding="utf-8")

    def test_valid_local_reference(self):
        (self.root / "OTHER.md").write_text("Valid", encoding="utf-8")
        (self.root / "README.md").write_text("[Go](OTHER.md)", encoding="utf-8")
        self.assertEqual(validate_links(self.root, ["README.md"]), [])

    def test_missing_local_reference_reported(self):
        (self.root / "README.md").write_text("[Go](missing.md)", encoding="utf-8")
        result = validate_links(self.root, ["README.md"])
        self.assertEqual(len(result), 1)
        self.assertIn("missing.md", result[0])

    def test_external_urls_not_treated_as_local_paths(self):
        refs = list(relative_targets("[Web](https://example.org/a) [Mail](mailto:x@y.z) [Top](#intro)"))
        self.assertEqual(refs, [])

    def test_asset_image_is_checked(self):
        (self.root / "README.md").write_text(
            '<img src="assets/missing.svg" alt="image" />', encoding="utf-8"
        )
        self.assertEqual(len(validate_links(self.root, ["README.md"])), 1)

    def test_directory_traversal_rejected(self):
        (self.root / "README.md").write_text("[Go](../private.txt)", encoding="utf-8")
        self.assertIn("escapes repository", validate_links(self.root, ["README.md"])[0])

    def test_example_links_in_code_fence_are_skipped(self):
        fence = chr(96) * 3
        text = f"{fence}markdown\n[example](missing.md)\n{fence}\n"
        self.assertEqual(list(relative_targets(text)), [])

    def test_valid_svg(self):
        (self.root / "assets" / "ok.svg").write_text(
            '<svg xmlns="http://www.w3.org/2000/svg"><rect width="5" height="5"/></svg>',
            encoding="utf-8",
        )
        self.assertEqual(validate_svg(self.root), [])

    def test_malformed_svg(self):
        (self.root / "assets" / "bad.svg").write_text("<svg><rect></svg>", encoding="utf-8")
        self.assertTrue(validate_svg(self.root))

    def test_active_content_rejected(self):
        (self.root / "assets" / "bad.svg").write_text(
            '<svg xmlns="http://www.w3.org/2000/svg"><script>x</script></svg>',
            encoding="utf-8",
        )
        self.assertIn("active content", validate_svg(self.root)[0])


if __name__ == "__main__":
    unittest.main()
