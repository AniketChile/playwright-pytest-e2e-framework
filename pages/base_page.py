"""Base page with reusable actions for all page objects."""

from pathlib import Path

from playwright.sync_api import Page, expect

from utils.logger import get_logger


class BasePage:
    """Base class providing shared browser interactions."""

    def __init__(self, page: Page) -> None:
        self.page = page
        self.logger = get_logger(self.__class__.__name__)

    def navigate(self, url: str) -> None:
        """Navigate to a URL and wait for load state."""
        self.logger.info(f"Navigating to: {url}")
        self.page.goto(url, wait_until="domcontentloaded")

    def click(self, selector: str) -> None:
        """Click an element after waiting for it."""
        self.logger.debug(f"Click: {selector}")
        self.page.locator(selector).click()

    def fill(self, selector: str, value: str) -> None:
        """Fill input field."""
        self.logger.debug(f"Fill: {selector}")
        self.page.locator(selector).fill(value)

    def get_text(self, selector: str) -> str:
        """Return inner text of an element."""
        return self.page.locator(selector).inner_text().strip()

    def is_visible(self, selector: str) -> bool:
        """Check if element is visible (non-blocking)."""
        return self.page.locator(selector).is_visible()

    def expect_visible(self, selector: str) -> None:
        """Assert element is visible using Playwright auto-wait."""
        expect(self.page.locator(selector)).to_be_visible()

    def expect_text(self, selector: str, text: str) -> None:
        """Assert element contains text."""
        expect(self.page.locator(selector)).to_contain_text(text)

    def wait_for_url(self, pattern: str) -> None:
        """Wait until URL matches pattern."""
        expect(self.page).to_have_url(pattern)

    def screenshot(self, name: str) -> None:
        """Save screenshot to reports/screenshots."""
        path = Path("reports/screenshots")
        path.mkdir(parents=True, exist_ok=True)
        self.page.screenshot(path=path / f"{name}.png")
