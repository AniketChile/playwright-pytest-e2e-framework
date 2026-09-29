"""Inventory (products) page object."""

from playwright.sync_api import Page

from pages.base_page import BasePage


class InventoryPage(BasePage):
    """SauceDemo products listing page."""

    TITLE = ".title"
    ITEMS = ".inventory_item"
    ITEM_NAMES = ".inventory_item_name"
    ITEM_PRICES = ".inventory_item_price"
    ADD_TO_CART = "button[data-test^='add-to-cart']"
    CART_BADGE = ".shopping_cart_badge"
    CART_LINK = ".shopping_cart_link"
    SORT_DROPDOWN = "[data-test='product-sort-container']"

    def __init__(self, page: Page) -> None:
        super().__init__(page)

    def get_title(self) -> str:
        return self.get_text(self.TITLE)

    def get_item_count(self) -> int:
        return self.page.locator(self.ITEMS).count()

    def add_first_item(self) -> None:
        self.page.locator(self.ADD_TO_CART).first.click()

    def add_item_by_name(self, name: str) -> None:
        item = self.page.locator(".inventory_item", has_text=name)
        item.locator("button").click()

    def get_cart_count(self) -> int:
        if self.is_visible(self.CART_BADGE):
            return int(self.get_text(self.CART_BADGE))
        return 0

    def open_cart(self) -> None:
        self.click(self.CART_LINK)

    def sort_by(self, option: str) -> None:
        self.page.select_option(self.SORT_DROPDOWN, option)

    def get_product_names(self) -> list[str]:
        return self.page.locator(self.ITEM_NAMES).all_inner_texts()

    def get_product_prices(self) -> list[float]:
        raw = self.page.locator(self.ITEM_PRICES).all_inner_texts()
        return [float(p.replace("$", "")) for p in raw]
