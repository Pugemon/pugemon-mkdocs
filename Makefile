PYTHON ?= python3

.DEFAULT_GOAL := help
.PHONY: help test docs docs-serve clean

help:  ## список целей
	@grep -E '^[a-z-]+:.*## ' $(MAKEFILE_LIST) | awk -F':.*## ' '{printf "  %-12s %s\n", $$1, $$2}'

test:  ## тесты плагина (нужны пакеты из requirements-docs.txt)
	$(PYTHON) -m unittest discover -s tests -v

docs:  ## собрать демо-сайт в site/ (strict)
	mkdocs build --strict

docs-serve:  ## демо-сайт с автообновлением на http://127.0.0.1:8000
	mkdocs serve

clean:  ## удалить site/ и артефакты сборки
	rm -rf site build dist src/*.egg-info
	find . -name __pycache__ -prune -exec rm -rf {} +
