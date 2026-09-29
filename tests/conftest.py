"""Shared pytest fixtures and hooks."""

from collections.abc import Generator
from pathlib import Path

import pytest
from playwright.sync_api import Browser, BrowserContext, Page, sync_playwright

from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage
from utils.config import Config
from utils.logger import get_logger
from utils.test_data import Users

logger = get_logger("conftest")


@pytest.fixture(scope="session")
def playwright_instance() -> Generator:
    with sync_playwright() as p:
        yield p


@pytest.fixture(scope="session")
def browser(playwright_instance) -> Generator[Browser, None, None]:
    logger.info(f"Launching browser: {Config.BROWSER} (headless={Config.HEADLESS})")
    browser_type = getattr(playwright_instance, Config.BROWSER)
    browser = browser_type.launch(headless=Config.HEADLESS)
    yield browser
    browser.close()


@pytest.fixture(scope="function")
def context(browser: Browser) -> Generator[BrowserContext, None, None]:
    ctx = browser.new_context(viewport={"width": 1440, "height": 900})
    ctx.set_default_timeout(Config.DEFAULT_TIMEOUT)
    yield ctx
    ctx.close()


@pytest.fixture(scope="function")
def page(context: BrowserContext) -> Generator[Page, None, None]:
    p = context.new_page()
    yield p
    p.close()


@pytest.fixture(scope="function")
def logged_in_page(page: Page) -> Page:
    """Return a page already authenticated as standard user."""
    login = LoginPage(page)
    login.open()
    login.login(Users.STANDARD.username, Users.STANDARD.password)
    InventoryPage(page).wait_until_loaded()
    return page


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Capture screenshot on test failure."""
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        page = item.funcargs.get("page") or item.funcargs.get("logged_in_page")
        if page:
            path = Path("reports/screenshots")
            path.mkdir(parents=True, exist_ok=True)
            page.screenshot(path=path / f"FAILED_{item.name}.png")
            logger.error(f"Screenshot saved for failed test: {item.name}")
