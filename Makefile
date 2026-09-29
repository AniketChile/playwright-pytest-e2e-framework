.PHONY: install test test-smoke test-critical test-parallel report lint format clean

install:
	python3 -m venv venv
	. venv/bin/activate && pip install -r requirements-dev.txt && playwright install chromium

test:
	pytest

test-smoke:
	pytest -m smoke

test-critical:
	pytest -m critical

test-parallel:
	pytest -n 4

report:
	@xdg-open reports/report.html 2>/dev/null || echo "Open reports/report.html manually"

lint:
	ruff check .
	black --check .

format:
	ruff check . --fix
	black .

clean:
	rm -rf .pytest_cache .ruff_cache .mypy_cache reports/*.html reports/screenshots logs/*.log
	find . -type d -name __pycache__ -exec rm -rf {} +
