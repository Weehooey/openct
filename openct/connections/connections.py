"""Module for connection protocols"""

from typing import Protocol
import logging

from fabric import Connection as FabricConnection
from paramiko.ssh_exception import (
    SSHException,
    NoValidConnectionsError,
    BadHostKeyException,
    AuthenticationException,
)
from invoke import UnexpectedExit, Failure

from openct.setup import Config


class DeviceConnection(Protocol):
    """DeviceConnection abstract base class"""

    def test_connection(self) -> bool:
        ...

    def get_backup(self, config_file: str, file_extension: str) -> None:
        ...

    def run_command(self, command: str) -> None:
        ...


class SshConnection(DeviceConnection):
    """DeviceConnection using Fabric"""

    def __init__(self, ip_address: str, config: Config) -> None:
        self.ip_address = ip_address
        self.username = config.identity.username
        self.connection_timeout = config.settings.connection_timeout
        self.key_file = config.identity.key_file
        self.backup_dir = config.dirs.backup_dir

    def test_connection(self) -> bool:
        with FabricConnection(
            host=self.ip_address,
            user=self.username,
            connect_timeout=self.connection_timeout,
            connect_kwargs={"key_filename": self.key_file},
        ) as connection:
            try:
                connection.open()
                return True
            except (
                TimeoutError,
                BadHostKeyException,
                AuthenticationException,
                SSHException,
                NoValidConnectionsError,
            ) as error:
                logging.error("Could not connect to device %s", self.ip_address)
                logging.info(error)
                return False

    def get_backup(
        self,
        config_file: str,
        file_extension: str,
    ) -> None:
        with FabricConnection(
            host=self.ip_address,
            user=self.username,
            connect_timeout=self.connection_timeout,
            connect_kwargs={"key_filename": self.key_file},
        ) as connection:
            try:
                connection.get(
                    config_file,
                    f"{self.backup_dir}/backup_{self.ip_address}{file_extension}",
                )
            except (UnexpectedExit, Failure) as error:
                logging.error(
                    "Error while getting backup from device %s", self.ip_address
                )
                logging.info(error)

    def run_command(self, command: str) -> None:
        with FabricConnection(
            host=self.ip_address,
            user=self.username,
            connect_timeout=self.connection_timeout,
            connect_kwargs={"key_filename": self.key_file},
        ) as connection:
            try:
                connection.run(
                    command,
                    hide=True,
                    warn=False,
                    timeout=self.connection_timeout,
                )
            except (UnexpectedExit, Failure) as error:
                logging.error(
                    "Error while running command: %s on %s", command, self.ip_address
                )
                logging.info(error)
