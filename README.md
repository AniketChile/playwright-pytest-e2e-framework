# Playwright + Pytest E2E Automation Framework

![CI](https://github.com/AniketChile/playwright-pytest-e2e-framework/actions/workflows/ci.yml/badge.svg)
![Python](https://img.shields.io/badge/python-3.11%20%7C%203.12-blue)
![Playwright](https://img.shields.io/badge/playwright-1.44-green)
![License](https://img.shields.io/badge/license-MIT-lightgrey)

Production-grade E2E automation framework built with Playwright, pytest, and the Page Object Model pattern. Automates critical user journeys on [SauceDemo](https://www.saucedemo.com/).

## 🎯 Why this exists

Manual regression is slow, error-prone, and blocks releases. This framework provides fast, isolated, parallelizable end-to-end coverage with CI integration and failure diagnostics.

## 🛠 Tech Stack

- **Python 3.11+**
- **Playwright** — modern, auto-waiting browser automation
- **pytest** — fixtures, markers, parametrization
- **pytest-html** — self-contained HTML reports
- **pytest-xdist** — parallel execution
- **Ruff + Black** — linting & formatting
- **GitHub Actions** — CI on every push/PR

## 🏗 Architecture

- **Tests** describe what to verify
- **Pages** encapsulate locators + interactions
- **Fixtures** manage browser lifecycle
- **Config** centralizes environment settings

## 📦 Setup

```bash
git clone https://github.com/<your-username>/playwright-pytest-e2e-framework.git
cd playwright-pytest-e2e-framework

python3 -m venv venv
source venv/bin/activate
pip install -r requirements-dev.txt
playwright install chromium
cp .env.example .env
pre-commit install