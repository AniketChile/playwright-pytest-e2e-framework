"""Cart page object."""

from playwright.sync_api import Page

from pages.base_page import BasePage


class CartPage(BasePage):
    """SauceDemo shopping cart page."""

    CART_ITEMS = ".cart_item"
    CHECKOUT_BUTTON = "#checkout"
    CONTINUE_SHOPPING = "#continue-shopping"
    REMOVE_BUTTONS = "button[data-test^='remove']"

    def __init__(self, page: Page) -> None:
        super().__init__(page)

    def get_item_count(self) -> int:
        return self.page.locator(self.CART_ITEMS).count()

    def remove_first_item(self) -> None:
        self.page.locator(self.REMOVE_BUTTONS).first.click()

    def checkout(self) -> None:
        self.click(self.CHECKOUT_BUTTON)

    def continue_shopping(self) -> None:
        self.click(self.CONTINUE_SHOPPING)
