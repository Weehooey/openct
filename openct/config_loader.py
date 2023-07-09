"""Config loader module."""

from dataclasses import dataclass
import sys

import yaml

CONFIG_FILE = "config/config.yml"


@dataclass
class ConfigIdentity:
    """Config identity dataclass."""

    username: str
    key_file: str


@dataclass
class ConfigDirs:
    """Config directories dataclass."""

    backup_dir: str
    log_dir: str


@dataclass
class ConfigSettings:
    """Config settings dataclass."""

    connection_timeout: int
    backup_max_age: int
    log_max_age: int
    log_max_count: int


@dataclass
class Config:
    """Config dataclass."""

    identity: ConfigIdentity
    dirs: ConfigDirs
    settings: ConfigSettings


def load_config() -> Config:
    """Try loading config."""
    try:
        return load_config_from_file()
    except FileNotFoundError:
        print(f"Config file {CONFIG_FILE} not found. Please create it.")
        sys.exit(1)
    except TypeError:
        print(f"Config file {CONFIG_FILE} is empty. Please populate it.")
        sys.exit(1)


def load_config_from_file() -> Config:
    """Load config from file."""
    with open(file=CONFIG_FILE, mode="r", encoding="utf-8") as config_file:
        config_data = yaml.safe_load(config_file)

    identity = ConfigIdentity(
        username=config_data["identity"]["username"],
        key_file=config_data["identity"]["key_file"],
    )

    dirs = ConfigDirs(
        backup_dir=config_data["directories"]["backup_dir"],
        log_dir=config_data["directories"]["log_dir"],
    )

    settings = ConfigSettings(
        connection_timeout=config_data["settings"]["connection_timeout"],
        backup_max_age=config_data["settings"]["backup_max_age"],
        log_max_age=config_data["settings"]["log_max_age"],
        log_max_count=config_data["settings"]["log_max_count"],
    )

    return Config(identity=identity, dirs=dirs, settings=settings)


if __name__ == "__main__":
    mt_backup_config = {
        "identity": {
            "username": "mtbackup",
            "key_file": "config/.ssh/id_rsa",
        },
        "dirs": {
            "backup_dir": "backups",
            "log_dir": "log/mt-config-backup",
        },
        "settings": {
            "connection_timeout": 3,
            "backup_max_age": 60,
            "log_max_count": 10,
        },
    }

    with open(file=CONFIG_FILE, mode="a", encoding="utf-8") as file:
        yaml.dump(mt_backup_config, file, default_flow_style=False)
