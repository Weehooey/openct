"""Config file generator."""

import yaml


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

with open(file="config/config.yml", mode="a", encoding="utf-8") as file:
    yaml.dump(mt_backup_config, file, default_flow_style=False)
