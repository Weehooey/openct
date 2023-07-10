"""Config types schema."""

from dataclasses import dataclass


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

    datastore_type: str
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
