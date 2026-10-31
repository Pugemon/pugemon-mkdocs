"""Плагин MkDocs ``pugemon``: тема Pugemon поверх Material for MkDocs.

При загрузке конфига плагин:

* ставит каталог темы (шаблон 404, стили, знак) сразу после ``custom_dir`` проекта —
  переопределения самого проекта остаются главнее;
* добавляет стили темы в начало ``extra_css``;
* задаёт схемы ``pugemon-dark`` / ``pugemon-light``, шрифты IBM Plex, знак и фавикон —
  только там, где проект не указал своё.
"""

from __future__ import annotations

from pathlib import Path

from mkdocs.config import config_options as opt
from mkdocs.config.base import Config
from mkdocs.exceptions import PluginError
from mkdocs.plugins import BasePlugin, get_plugin_logger

THEME_DIR = Path(__file__).parent / "theme"
STYLES = ["assets/pugemon/pugemon.css", "assets/pugemon/mermaid.css"]
LOGO = "assets/pugemon/logo.png"
FAVICON = "assets/pugemon/favicon.png"

# Значения из mkdocs_theme.yml Material: их плагин считает «не заданными проектом».
MATERIAL_FONT = {"text": "Roboto", "code": "Roboto Mono"}
MATERIAL_FAVICON = "assets/images/favicon.png"
PLEX_FONT = {"text": "IBM Plex Sans", "code": "IBM Plex Mono"}

log = get_plugin_logger(__name__)


class PugemonConfig(Config):
    scheme = opt.Choice(("auto", "dark", "light"), default="auto")
    toggle = opt.Type(bool, default=True)
    fonts = opt.Type(bool, default=True)
    logo = opt.Type(bool, default=True)


def build_palette(scheme: str, toggle: bool, russian: bool) -> list[dict] | dict:
    """Палитра Material для схем Pugemon.

    auto — по настройке системы (без предпочтения — тёмная), dark / light — с этой схемы
    начинается сайт; toggle — переключатель в шапке.
    """
    names = {"dark": "Тёмная тема", "light": "Светлая тема"} if russian else \
            {"dark": "Dark mode", "light": "Light mode"}
    icons = {"dark": "material/weather-night", "light": "material/weather-sunny"}
    order = ["light", "dark"] if scheme == "light" else ["dark", "light"]
    if not toggle:
        return {"scheme": f"pugemon-{order[0]}"}
    palette = []
    for current, other in (order, order[::-1]):
        entry = {"scheme": f"pugemon-{current}",
                 "toggle": {"icon": icons[other], "name": names[other]}}
        if scheme == "auto":
            entry = {"media": f"(prefers-color-scheme: {current})", **entry}
        palette.append(entry)
    return palette


class PugemonPlugin(BasePlugin[PugemonConfig]):
    def on_config(self, config):
        theme = config.theme
        if theme.name != "material":
            raise PluginError(f"pugemon: нужна тема material, а в mkdocs.yml указана {theme.name!r}")

        theme.dirs.insert(1 if theme.custom_dir else 0, str(THEME_DIR))
        config.extra_css[:0] = [s for s in STYLES if s not in config.extra_css]

        if theme.get("palette"):
            log.debug("palette задана в проекте — оставлена как есть")
        else:
            russian = str(theme.get("language", "en")).startswith("ru")
            theme["palette"] = build_palette(self.config.scheme, self.config.toggle, russian)

        if self.config.fonts and theme.get("font") == MATERIAL_FONT:
            theme["font"] = dict(PLEX_FONT)

        if self.config.logo:
            if not theme.get("logo") and not (theme.get("icon") or {}).get("logo"):
                theme["logo"] = LOGO
            if theme.get("favicon") in (None, MATERIAL_FAVICON):
                theme["favicon"] = FAVICON
        return config
