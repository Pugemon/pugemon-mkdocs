# pugemon-mkdocs

A documentation theme for [MkDocs Material](https://squidfunk.github.io/mkdocs-material/) in the
colors of the Pugemon design system: Gruvbox, cyan links, signature yellow, IBM Plex Sans and Mono.
Dark scheme first, light scheme via the toggle or the system preference.

Русская версия: [README.md](README.md) · Demo: <https://pugemon.github.io/pugemon-mkdocs/>

## Usage

`requirements-docs.txt`:

```text
mkdocs-material==9.7.7
pugemon-mkdocs @ git+https://github.com/pugemon/pugemon-mkdocs.git@v0.1.0
```

`mkdocs.yml`:

```yaml
theme:
  name: material

plugins:
  - search
  - pugemon
```

The `pugemon` plugin adds the stylesheets, the `pugemon-dark` / `pugemon-light` schemes, fonts,
the pixel logo, the favicon and a 404 page — nothing has to be copied into your project.
Anything your project sets in `theme` itself (`palette`, `font`, `logo`, `favicon`, templates in
`custom_dir`) takes precedence.

Plugin options: `scheme` (`auto` | `dark` | `light`), `toggle`, `fonts`, `logo` — all described
(in Russian) on the [usage page](https://pugemon.github.io/pugemon-mkdocs/usage/).

## License

BSD-3-Clause, see [LICENSE](LICENSE).
