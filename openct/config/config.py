"""Config """

import sys

import yaml

from .config_schema import Config, ConfigDirs, ConfigIdentity, ConfigSettings


def load_config(config_file: str = "config/config.yml") -> Config:
    """Try loading config."""
    try:
        return load_config_from_file(config_file)
    except FileNotFoundError:
        print(f"Config file {config_file} not found. Please create it.")
        sys.exit(1)
    except TypeError:
        print(f"Config file {config_file} is empty. Please populate it.")
        sys.exit(1)


def load_config_from_file(config_file: str) -> Config:
    """Load config from file."""
    with open(file=config_file, mode="r", encoding="utf-8") as conf_file:
        config_data = yaml.safe_load(conf_file)

    identity = ConfigIdentity(
        username=config_data["identity"]["username"],
        key_file=config_data["identity"]["key_file"],
    )

    dirs = ConfigDirs(
        backup_dir=config_data["dirs"]["backup_dir"],
        log_dir=config_data["dirs"]["log_dir"],
    )

    settings = ConfigSettings(
        datastore_type=config_data["settings"]["datastore_type"],
        connection_timeout=config_data["settings"]["connection_timeout"],
        backup_max_age=config_data["settings"]["backup_max_age"],
        log_max_age=config_data["settings"]["log_max_age"],
        log_max_count=config_data["settings"]["log_max_count"],
    )

    return Config(identity=identity, dirs=dirs, settings=settings)
