"""Checkout test suite."""

import pytest

from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.inventory_page import InventoryPage
from utils.test_data import CheckoutData


@pytest.mark.regression
@pytest.mark.critical
class TestCheckout:
    """Covers end-to-end checkout flow."""

    def _reach_checkout(self, page) -> CheckoutPage:
        inv = InventoryPage(page)
        inv.add_first_item()
        inv.open_cart()
        CartPage(page).checkout()
        return CheckoutPage(page)

    def test_full_checkout_happy_path(self, logged_in_page) -> None:
        checkout = self._reach_checkout(logged_in_page)
        info = CheckoutData.VALID
        checkout.fill_info(info["first_name"], info["last_name"], info["postal_code"])
        checkout.continue_to_overview()
        checkout.finish_order()
        assert "Thank you for your order" in checkout.get_complete_message()

    @pytest.mark.parametrize(
        "data,expected_error",
        [
            (CheckoutData.MISSING_FIRST, "First Name is required"),
            (CheckoutData.MISSING_LAST, "Last Name is required"),
            (CheckoutData.MISSING_ZIP, "Postal Code is required"),
        ],
    )
    def test_checkout_validation(self, logged_in_page, data, expected_error) -> None:
        checkout = self._reach_checkout(logged_in_page)
        checkout.fill_info(data["first_name"], data["last_name"], data["postal_code"])
        checkout.continue_to_overview()
        assert expected_error in checkout.get_error()
