"""Inventory test suite."""

import pytest

from pages.inventory_page import InventoryPage
from utils.helpers import is_sorted
from utils.test_data import SortOptions


@pytest.mark.regression
class TestInventory:
    """Covers product listing behavior."""

    def test_inventory_loads_six_products(self, logged_in_page) -> None:
        assert InventoryPage(logged_in_page).get_item_count() == 6

    def test_add_single_item(self, logged_in_page) -> None:
        inv = InventoryPage(logged_in_page)
        inv.add_first_item()
        assert inv.get_cart_count() == 1

    def test_sort_price_low_to_high(self, logged_in_page) -> None:
        inv = InventoryPage(logged_in_page)
        inv.sort_by(SortOptions.PRICE_ASC)
        assert is_sorted(inv.get_product_prices())

    def test_sort_price_high_to_low(self, logged_in_page) -> None:
        inv = InventoryPage(logged_in_page)
        inv.sort_by(SortOptions.PRICE_DESC)
        assert is_sorted(inv.get_product_prices(), reverse=True)

    def test_sort_name_z_to_a(self, logged_in_page) -> None:
        inv = InventoryPage(logged_in_page)
        inv.sort_by(SortOptions.NAME_DESC)
        assert is_sorted(inv.get_product_names(), reverse=True)
