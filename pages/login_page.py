"""Login page object."""

from playwright.sync_api import Page

from pages.base_page import BasePage


class LoginPage(BasePage):
    """SauceDemo login page."""

    URL = "https://www.saucedemo.com/"

    USERNAME_INPUT = "#user-name"
    PASSWORD_INPUT = "#password"
    LOGIN_BUTTON = "#login-button"
    ERROR_MESSAGE = "[data-test='error']"

    def __init__(self, page: Page) -> None:
        super().__init__(page)

    def open(self) -> "LoginPage":
        """Open the login page."""
        self.navigate(self.URL)
        return self

    def login(self, username: str, password: str) -> None:
        """Perform login with given credentials."""
        self.fill(self.USERNAME_INPUT, username)
        self.fill(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)

    def get_error(self) -> str:
        """Return error message text."""
        return self.get_text(self.ERROR_MESSAGE)

    def has_error(self) -> bool:
        """Return True if error banner is visible."""
        return self.is_visible(self.ERROR_MESSAGE)
