# pugemon-mkdocs

[![ci](https://github.com/pugemon/pugemon-mkdocs/actions/workflows/ci.yml/badge.svg)](https://github.com/pugemon/pugemon-mkdocs/actions/workflows/ci.yml)
[![docs](https://github.com/pugemon/pugemon-mkdocs/actions/workflows/docs.yml/badge.svg)](https://pugemon.github.io/pugemon-mkdocs/)
[![license](https://img.shields.io/badge/license-BSD--3--Clause-076678)](LICENSE)

Тема документации для [MkDocs Material](https://squidfunk.github.io/mkdocs-material/) в цветах
дизайн-системы Pugemon: Gruvbox, бирюза для ссылок и фирменный жёлтый, IBM Plex Sans и Mono.
Тёмная схема основная, светлая включается переключателем или по настройке системы.

English: [README.en.md](README.en.md) · Демо: <https://pugemon.github.io/pugemon-mkdocs/>

## Подключение

`requirements-docs.txt`:

```text
mkdocs-material==9.7.7
pugemon-mkdocs @ git+https://github.com/pugemon/pugemon-mkdocs.git@v0.1.0
```

`mkdocs.yml`:

```yaml
theme:
  name: material
  language: ru

plugins:
  - search
  - pugemon
```

Плагин сам добавляет стили, схемы `pugemon-dark` / `pugemon-light`, шрифты, пиксельный знак,
фавикон и страницу 404 — копировать файлы в проект не нужно. Всё, что проект задал в `theme`
сам (`palette`, `font`, `logo`, `favicon`, свои шаблоны в `custom_dir`), остаётся главнее.
Настройки плагина и рекомендуемые расширения Markdown — на странице
[«Подключение»](https://pugemon.github.io/pugemon-mkdocs/usage/).

## Что внутри

```
src/pugemon_mkdocs/plugin.py                 плагин pugemon
src/pugemon_mkdocs/theme/404.html            страница 404 в чёрно-белом «режиме кино»
src/pugemon_mkdocs/theme/assets/pugemon/     pugemon.css — сама тема, mermaid.css — схемы,
                                             logo.png (256×256), favicon.png (32×32), favicon-64.png
docs/                                        демо-сайт: все перекрашенные элементы на Python, C++ и Go
tests/                                       сборка маленьких сайтов с плагином
```

## Разработка

```console
$ python3 -m venv .venv && . .venv/bin/activate
$ pip install -r requirements-docs.txt     # mkdocs, material и тема в режиме -e
$ make test                                # тесты плагина
$ make docs-serve                          # демо-сайт на http://127.0.0.1:8000
```

## Где используется

[mailcow-shared-mailboxes](https://github.com/pugemon/mailcow-shared-mailboxes) ·
[mailcow-migration-tools](https://github.com/pugemon/mailcow-migration-tools) ·
[mailcow-edge-gateway](https://github.com/pugemon/mailcow-edge-gateway) ·
[mail-domain-check](https://github.com/pugemon/mail-domain-check)

## Лицензия

BSD-3-Clause, см. [LICENSE](LICENSE). Material for MkDocs распространяется под собственной
лицензией MIT и в этот репозиторий не входит.
