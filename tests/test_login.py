"""Login test suite."""
import pytest

from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage
from utils.test_data import Users


@pytest.mark.smoke
@pytest.mark.critical
class TestLogin:
    """Covers authentication scenarios."""

    def test_valid_login(self, page) -> None:
        login = LoginPage(page)
        login.open()
        login.login(Users.STANDARD.username, Users.STANDARD.password)
        inventory = InventoryPage(page)
        assert inventory.get_title() == "Products"

    def test_locked_out_user(self, page) -> None:
        login = LoginPage(page)
        login.open()
        login.login(Users.LOCKED.username, Users.LOCKED.password)
        assert login.has_error()
        assert "locked out" in login.get_error().lower()

    def test_invalid_credentials(self, page) -> None:
        login = LoginPage(page)
        login.open()
        login.login(Users.INVALID.username, Users.INVALID.password)
        assert login.has_error()
        assert "do not match" in login.get_error().lower()

    @pytest.mark.parametrize(
        "username,password,expected",
        [
            ("", "secret_sauce", "Username is required"),
            ("standard_user", "", "Password is required"),
        ],
    )
    def test_empty_credentials(self, page, username, password, expected) -> None:
        login = LoginPage(page)
        login.open()
        login.login(username, password)
        assert expected.lower() in login.get_error().lower()
