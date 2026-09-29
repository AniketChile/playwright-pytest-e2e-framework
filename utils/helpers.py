"""Reusable helper utilities."""

import re


def parse_price(text: str) -> float:
    """Convert '$12.99' to 12.99."""
    match = re.search(r"[\d.]+", text)
    if not match:
        raise ValueError(f"Cannot parse price from: {text}")
    return float(match.group())


def is_sorted(items: list, reverse: bool = False) -> bool:
    """Return True if list is sorted in given direction."""
    return items == sorted(items, reverse=reverse)
