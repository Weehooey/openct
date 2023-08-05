"""Config file generator."""

import os
import sys

import yaml

CONFIG_FILE = "config.yml"

if os.path.exists(CONFIG_FILE):
    user_input = input(
        f"The config file '{CONFIG_FILE}' already exists. Do you want to overwrite it? (yes/no): "
    ).lower()
    if user_input not in {"yes", "y"}:
        print("Config file not overwritten. Exiting.")
        sys.exit()
    os.rename(CONFIG_FILE, CONFIG_FILE + ".bak")

starting_config_values = {
    "config_version": {
        "version": "0.1.0",
        "comments": "Inital config verion."
    },
    "identity": {
        "username": "username",
        "key_file": "config/.ssh/id_rsa",
    },
    "dirs": {
        "backup_dir": "backups",
        "log_dir": "logs",
    },
    "settings": {
        "datastore_type": "yaml",
        "connection_timeout": 3,
        "backup_max_age": 60,
        "log_max_age": 30,
        "log_max_count": 10,
    },
}

with open(file="config.yml", mode="w", encoding="utf-8") as file:
    yaml.dump(starting_config_values, file, default_flow_style=False)
