"""Setup
"""

import os
import time
import logging
import argparse
import platform

import openct
from .config_schema import Config
from .config import load_config


def setup_config() -> Config:
    args = parse_args()

    config: Config = load_config(os.path.join(args.root, args.config_file))
    config.dirs.root_dir = args.root

    init_logging(config.dirs.log_dir)

    config.dirs.backup_dir = os.path.join(
        config.dirs.backup_dir, time.strftime("%Y%m%d_%H%M")
    )

    return config


def parse_args():
    parser = argparse.ArgumentParser(description="Your program description here.")
    parser.add_argument(
        "--root",
        metavar="PATH",
        default=".",
        help="Specify the root directory for your program (default: current directory).",
    )
    parser.add_argument(
        "--config",
        metavar="FILE",
        dest="config_file",
        default="config.yml",
        help="Config file for the program (default: config.yml). Uses root path.",
    )

    args = parser.parse_args()
    return args


def init_logging(log_dir: str) -> None:
    log_file = os.path.join(log_dir, f"ocb_{time.strftime('%Y%m%d_%H%M%S')}.log")

    header_info = f"Package Version: {openct.__version__}\n"
    header_info += f"OS: {platform.system()} {platform.release()}\n"
    header_info += f"Python Version: {platform.python_version()}\n"
    header_info += "\n"

    with open(log_file, "a", encoding="utf-8") as file:
        file.write(header_info)

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(module)s] [%(levelname)s] %(message)s",
        filename=log_file,
        filemode="a",
        encoding="utf-8",
    )
