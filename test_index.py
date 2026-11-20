"""Unit tests for the Bob Apache httpd webpage (index.html).

Validates that the static HTML content contains the required title, headings,
and key content about Bob running on IBM Fusion on-prem at the Arrow
Experience Center, served from an Apache httpd container.
"""

import os
import unittest

INDEX_PATH = os.path.join(os.path.dirname(__file__), "index.html")


class TestIndexHtml(unittest.TestCase):
    """Tests for index.html content."""

    @classmethod
    def setUpClass(cls):
        with open(INDEX_PATH, "r", encoding="utf-8") as f:
            cls.html = f.read()

    def test_file_exists(self):
        self.assertTrue(os.path.isfile(INDEX_PATH))

    def test_doctype(self):
        self.assertIn("<!DOCTYPE html>", self.html)

    def test_title(self):
        self.assertIn(
            "Bob — IBM Fusion on-prem at Arrow Experience Center", self.html
        )

    def test_h1_bob(self):
        self.assertIn("<h1>Bob</h1>", self.html)

    def test_subtitle(self):
        self.assertIn(
            "Apache httpd container · IBM Fusion on-prem · Arrow Experience Center",
            self.html,
        )

    def test_badges_present(self):
        for badge in [
            "Apache httpd",
            "Container",
            "IBM Fusion",
            "On-prem",
            "Arrow Experience Center",
        ]:
            with self.subTest(badge=badge):
                self.assertIn(f">{badge}</span>", self.html)

    def test_about_bob_section(self):
        self.assertIn("<h2>About Bob</h2>", self.html)
        self.assertIn("AI-powered software engineering agent", self.html)

    def test_ibm_fusion_section(self):
        self.assertIn("<h2>Running on IBM Fusion on-prem</h2>", self.html)
        self.assertIn("IBM Fusion on-premises infrastructure", self.html)
        self.assertIn("Apache httpd container", self.html)

    def test_arrow_experience_center_section(self):
        self.assertIn("<h2>Arrow Experience Center</h2>", self.html)
        self.assertIn("Arrow Experience Center", self.html)
        self.assertIn("containerized workload", self.html)

    def test_footer(self):
        self.assertIn("Made with IBM Bob", self.html)
        self.assertIn("Apache httpd container", self.html)
        self.assertIn("IBM Fusion on-prem", self.html)
        self.assertIn("Arrow Experience Center", self.html)


if __name__ == "__main__":
    unittest.main()