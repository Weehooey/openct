"""Logging init module."""

import logging
import os
import time


def init_logger(log_dir) -> None:
    """Initialize logger."""
    log_file = os.path.join(log_dir, f"ocb_{time.strftime('%Y%m%d_%H%M%S')}.log")

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(module)s] [%(levelname)s] %(message)s",
        filename=log_file,
        filemode="a",
        encoding="utf-8",
    )
