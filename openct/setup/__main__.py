"""Config file generator."""

import os

import yaml

CONFIG_FILE = "config.yml"

if os.path.exists(CONFIG_FILE):
    user_input = input(
        f"The config file '{CONFIG_FILE}' already exists. Do you want to overwrite it? (yes/no): "
    ).lower()
    if user_input != "yes" and user_input != "y":
        print("Config file not overwritten. Exiting.")
        exit()

mt_backup_config = {
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

with open(file=CONFIG_FILE, mode="w", encoding="utf-8") as file:
    yaml.dump(mt_backup_config, file, default_flow_style=False)
