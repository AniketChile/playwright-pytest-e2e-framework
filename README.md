# Playwright + Pytest E2E Automation Framework

[![CI](https://github.com/AniketChile/playwright-pytest-e2e-framework/actions/workflows/ci.yml/badge.svg)](https://github.com/AniketChile/playwright-pytest-e2e-framework/actions/workflows/ci.yml)
![Python](https://img.shields.io/badge/python-3.11%20%7C%203.12-blue)
![Playwright](https://img.shields.io/badge/playwright-1.44-green)
![License](https://img.shields.io/badge/license-MIT-lightgrey)

A maintainable end-to-end test automation framework built with Python, Playwright,
and Pytest. It validates critical user journeys on
[SauceDemo](https://www.saucedemo.com/) using the Page Object Model pattern.

## What this demonstrates

- Reusable Page Object Model design with shared browser actions
- Isolated Pytest fixtures for browser, context, and page lifecycles
- Positive, negative, and parametrized test scenarios
- Environment-driven configuration without hard-coded runtime settings
- HTML reporting and failure screenshots for faster debugging
- Smoke, regression, and critical test markers
- Parallel execution with `pytest-xdist`
- Ruff and Black quality gates
- GitHub Actions CI across Python 3.11 and 3.12

## Tech stack

- **Python 3.11+**
- **Playwright** for browser automation
- **Pytest** for test execution, fixtures, and parametrization
- **pytest-html** for self-contained HTML reports
- **pytest-xdist** for parallel execution
- **Ruff + Black** for linting and formatting
- **GitHub Actions** for continuous integration

## Coverage

| Area | Scenarios |
| --- | --- |
| Authentication | Valid login, locked user, invalid credentials, required fields |
| Inventory | Product count, add to cart, price sorting, name sorting |
| Cart | Add item, remove item, continue shopping |
| Checkout | Successful order and required-field validation |

The suite currently contains **17 end-to-end tests**.

## Project structure

```text
.
├── pages/                 # Page Object Model classes
├── tests/                 # Test cases and shared Pytest fixtures
├── utils/                 # Configuration, logging, helpers, and test data
├── .github/workflows/     # GitHub Actions CI pipeline
├── Makefile               # Common local commands
├── pyproject.toml         # Pytest, Ruff, Black, and Mypy configuration
└── requirements*.txt      # Runtime and development dependencies
```

## Local setup

```bash
git clone https://github.com/AniketChile/playwright-pytest-e2e-framework.git
cd playwright-pytest-e2e-framework

python3 -m venv venv
source venv/bin/activate
pip install -r requirements-dev.txt
playwright install chromium
cp .env.example .env
pre-commit install
```

## Run tests

```bash
# Full suite
pytest

# Test groups
pytest -m smoke
pytest -m critical
pytest -m regression

# Run in parallel
pytest -n 4

# Common Makefile shortcuts
make test
make test-smoke
make test-critical
make test-parallel
```

Pytest writes a self-contained report to
[`reports/report.html`](reports/report.html). On failure, screenshots are saved
under `reports/screenshots/`, and execution logs are written to `logs/test.log`.
Generated reports and logs are intentionally ignored by Git.

## Configuration

Runtime settings can be changed in `.env`:

```dotenv
BASE_URL=https://www.saucedemo.com/
HEADLESS=true
BROWSER=chromium
DEFAULT_TIMEOUT=15000
LOG_LEVEL=INFO
PARALLEL_WORKERS=4
```

## Continuous integration

The GitHub Actions workflow runs on every push and pull request to `main` or
`develop`. It:

1. Runs Ruff and Black checks.
2. Executes the test suite on Python 3.11 and 3.12.
3. Installs Chromium with system dependencies.
4. Uploads the HTML report for every run.
5. Uploads failure screenshots when a test fails.

## Quality checks

```bash
make lint
make format
```

## License

This project is available under the MIT License.
