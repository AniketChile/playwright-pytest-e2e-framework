"""Environment-driven configuration."""
import os
from dataclasses import dataclass

from dotenv import load_dotenv

load_dotenv()


@dataclass(frozen=True)
class Config:
    """Immutable application configuration loaded from environment."""

    BASE_URL: str = os.getenv("BASE_URL", "https://www.saucedemo.com/")
    HEADLESS: bool = os.getenv("HEADLESS", "true").lower() == "true"
    BROWSER: str = os.getenv("BROWSER", "chromium")
    DEFAULT_TIMEOUT: int = int(os.getenv("DEFAULT_TIMEOUT", "15000"))
    LOG_LEVEL: str = os.getenv("LOG_LEVEL", "INFO")
    PARALLEL_WORKERS: int = int(os.getenv("PARALLEL_WORKERS", "4"))
