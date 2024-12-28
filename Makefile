sources = src/basilico src/tests

.PHONY: test
test:
	uv run coverage run -m pytest && uv run coverage report -m

.PHONY: benchmark
benchmark:
	uv run -m pytest -m benchmark

.PHONY: lint
lint:
	uv run ruff check $(sources)
	uv run ruff format --check $(sources)

.PHONY: format
format:
	uv run ruff check --fix $(sources)
	uv run ruff format $(sources)

.PHONY: typecheck
typecheck:
	uv run pyright -p pyproject.toml
