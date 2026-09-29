"""Static test data - no credentials in test files."""

from dataclasses import dataclass


@dataclass(frozen=True)
class User:
    username: str
    password: str


class Users:
    STANDARD = User("standard_user", "secret_sauce")
    LOCKED = User("locked_out_user", "secret_sauce")
    PROBLEM = User("problem_user", "secret_sauce")
    PERFORMANCE = User("performance_glitch_user", "secret_sauce")
    INVALID = User("invalid_user", "wrong_password")


class CheckoutData:
    VALID = {"first_name": "John", "last_name": "Doe", "postal_code": "12345"}
    MISSING_FIRST = {"first_name": "", "last_name": "Doe", "postal_code": "12345"}
    MISSING_LAST = {"first_name": "John", "last_name": "", "postal_code": "12345"}
    MISSING_ZIP = {"first_name": "John", "last_name": "Doe", "postal_code": ""}


class SortOptions:
    NAME_ASC = "az"
    NAME_DESC = "za"
    PRICE_ASC = "lohi"
    PRICE_DESC = "hilo"
