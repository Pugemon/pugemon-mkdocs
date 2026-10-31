"""Сборка маленьких сайтов с плагином pugemon (нужны mkdocs, mkdocs-material и установленный пакет)."""

import re
import tempfile
import unittest
from pathlib import Path

from mkdocs.commands.build import build
from mkdocs.config import load_config
from mkdocs.exceptions import Abort, PluginError

from pugemon_mkdocs.plugin import build_palette

BASE = """\
site_name: demo
theme:
  name: {theme}
{theme_extra}
plugins:
  - pugemon{plugin_extra}
"""


class SiteTest(unittest.TestCase):
    def build(self, theme="material", theme_extra="", plugin_extra="", files=None):
        tmp = Path(tempfile.mkdtemp())
        (tmp / "docs").mkdir()
        (tmp / "docs" / "index.md").write_text("# Демо\n\nТекст.\n")
        for name, text in (files or {}).items():
            (tmp / name).parent.mkdir(parents=True, exist_ok=True)
            (tmp / name).write_text(text)
        (tmp / "mkdocs.yml").write_text(BASE.format(theme=theme, theme_extra=theme_extra,
                                                    plugin_extra=plugin_extra))
        build(load_config(config_file=str(tmp / "mkdocs.yml"), strict=True))
        return tmp / "site"

    def body(self, site):
        return re.search(r"<body[^>]*>", (site / "index.html").read_text())[0]

    def test_assets_styles_logo_fonts(self):
        site = self.build()
        for name in ("pugemon.css", "mermaid.css", "logo.png", "favicon.png"):
            self.assertTrue((site / "assets/pugemon" / name).is_file(), name)
        html = (site / "index.html").read_text()
        self.assertIn("assets/pugemon/pugemon.css", html)
        self.assertIn("assets/pugemon/logo.png", html)
        self.assertIn("IBM+Plex+Sans", html)
        self.assertIn('data-md-color-scheme="pugemon-dark"', self.body(site))

    def test_light_first(self):
        site = self.build(plugin_extra=":\n      scheme: light")
        self.assertIn('data-md-color-scheme="pugemon-light"', self.body(site))

    def test_project_settings_win(self):
        site = self.build(theme_extra="  palette:\n    scheme: slate\n  font:\n    text: Inter\n    code: Fira Code\n")
        html = (site / "index.html").read_text()
        self.assertIn('data-md-color-scheme="slate"', self.body(site))
        self.assertIn("Inter", html)
        self.assertNotIn("IBM+Plex+Sans", html)

    def test_custom_dir_wins(self):
        site = self.build(theme_extra="  custom_dir: overrides\n",
                          files={"overrides/404.html": "{% extends 'main.html' %}"
                                                       "{% block content %}СВОЯ-404{% endblock %}"})
        self.assertIn("СВОЯ-404", (site / "404.html").read_text())

    def test_theme_404(self):
        site = self.build()
        self.assertIn("pg-404", (site / "404.html").read_text())

    def test_requires_material(self):
        with self.assertRaises((PluginError, Abort)):   # build() оборачивает ошибку плагина в Abort
            self.build(theme="mkdocs")


class PaletteTest(unittest.TestCase):
    def test_auto(self):
        p = build_palette("auto", True, russian=True)
        self.assertEqual([e["scheme"] for e in p], ["pugemon-dark", "pugemon-light"])
        self.assertEqual(p[0]["media"], "(prefers-color-scheme: dark)")
        self.assertEqual(p[0]["toggle"]["name"], "Светлая тема")

    def test_fixed_without_toggle(self):
        self.assertEqual(build_palette("light", False, russian=False), {"scheme": "pugemon-light"})

    def test_dark_no_media(self):
        p = build_palette("dark", True, russian=False)
        self.assertNotIn("media", p[0])
        self.assertEqual(p[0]["toggle"]["name"], "Light mode")


if __name__ == "__main__":
    unittest.main()
