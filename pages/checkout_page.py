"""Checkout page object (info + overview + complete)."""

from playwright.sync_api import Page

from pages.base_page import BasePage


class CheckoutPage(BasePage):
    """SauceDemo checkout flow (3 steps)."""

    FIRST_NAME = "#first-name"
    LAST_NAME = "#last-name"
    POSTAL_CODE = "#postal-code"
    CONTINUE = "#continue"
    FINISH = "#finish"
    COMPLETE_HEADER = ".complete-header"
    SUMMARY_TOTAL = ".summary_total_label"
    ERROR = "[data-test='error']"

    def __init__(self, page: Page) -> None:
        super().__init__(page)

    def fill_info(self, first: str, last: str, zip_code: str) -> None:
        self.fill(self.FIRST_NAME, first)
        self.fill(self.LAST_NAME, last)
        self.fill(self.POSTAL_CODE, zip_code)

    def continue_to_overview(self) -> None:
        self.click(self.CONTINUE)

    def finish_order(self) -> None:
        self.click(self.FINISH)

    def get_complete_message(self) -> str:
        return self.get_text(self.COMPLETE_HEADER)

    def get_total(self) -> str:
        return self.get_text(self.SUMMARY_TOTAL)

    def get_error(self) -> str:
        return self.get_text(self.ERROR)
