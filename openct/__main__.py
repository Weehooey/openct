"""Main entry point for the OpenCT application."""

import yaml

from logging_init import init_logger
from config_loader import load_config
from backup import run_backup

DEVICES_FILE = "config/devices.yml"

config = load_config()

init_logger(config.dirs.log_dir)

with open(file=DEVICES_FILE, mode="r", encoding="utf-8") as file:
    devices = yaml.safe_load(file)

run_backup(config, devices["devices"])
