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


class DeviceConnection(Protocol):
    """DeviceConnection abstract base class"""

    def test_connection(self) -> bool:
        ...

    def fetch_backup(self) -> None:
        ...


class SshConnection(DeviceConnection):
    """DeviceConnection using Fabric"""

    def __init__(
        self,
        ip_address: str,
        username: str,
        connection_timeout: int,
        key_file: str,
        backup_dir: str,
    ) -> None:
        self.ip_address = ip_address
        self.username = username
        self.connection_timeout = connection_timeout
        self.key_file = key_file
        self.backup_dir = backup_dir

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
            ) as e:
                logging.error("Could not connect to device %s", self.ip_address)
                logging.info(e)
                return False

    def fetch_backup(self) -> None:
        with FabricConnection(
            host=self.ip_address,
            user=self.username,
            connect_timeout=self.connection_timeout,
            connect_kwargs={"key_filename": self.key_file},
        ) as connection:
            try:
                connection.run(
                    "/export file=backup",
                    hide=True,
                    warn=False,
                    timeout=self.connection_timeout,
                )
                connection.get(
                    "backup.rsc", f"{self.backup_dir}/backup_{self.ip_address}.rsc"
                )
                connection.run(
                    "file/remove backup.rsc",
                    hide=True,
                    warn=False,
                    timeout=self.connection_timeout,
                )
            except (UnexpectedExit, Failure) as e:
                logging.error(
                    "Error while fetching backup from device %s", self.ip_address
                )
                logging.info(e)
