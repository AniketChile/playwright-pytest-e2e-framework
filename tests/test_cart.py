"""Cart test suite."""
import pytest

from pages.cart_page import CartPage
from pages.inventory_page import InventoryPage


@pytest.mark.regression
class TestCart:
    """Covers cart operations."""

    def test_cart_shows_added_item(self, logged_in_page) -> None:
        inv = InventoryPage(logged_in_page)
        inv.add_first_item()
        inv.open_cart()
        assert CartPage(logged_in_page).get_item_count() == 1

    def test_remove_item(self, logged_in_page) -> None:
        inv = InventoryPage(logged_in_page)
        inv.add_first_item()
        inv.open_cart()
        cart = CartPage(logged_in_page)
        cart.remove_first_item()
        assert cart.get_item_count() == 0

    def test_continue_shopping(self, logged_in_page) -> None:
        inv = InventoryPage(logged_in_page)
        inv.add_first_item()
        inv.open_cart()
        CartPage(logged_in_page).continue_shopping()
        assert "inventory" in logged_in_page.url
