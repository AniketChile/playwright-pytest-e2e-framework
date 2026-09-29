"""Centralized logger factory."""
import logging
import sys
from pathlib import Path

from utils.config import Config


def get_logger(name: str) -> logging.Logger:
    """Return a configured logger writing to stdout and logs/test.log."""
    logger = logging.getLogger(name)
    if logger.handlers:
        return logger

    logger.setLevel(Config.LOG_LEVEL)
    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)-8s | %(name)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    stream = logging.StreamHandler(sys.stdout)
    stream.setFormatter(formatter)
    logger.addHandler(stream)

    log_dir = Path("logs")
    log_dir.mkdir(exist_ok=True)
    file_handler = logging.FileHandler(log_dir / "test.log")
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    return logger
