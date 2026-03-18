install:
	uv sync

run:
	uv run validator

test:
	uv run pytest

test-coverage:
	uv run pytest --cov=validator --cov-report xml

lint:
	uv run ruff check .

fix-lint:
	uv run ruff check --fix .

check: test lint

build:
	uv build

.PHONY: install test lint selfcheck check build
