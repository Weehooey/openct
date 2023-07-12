"""Module for connection protocols"""

from typing import Protocol

from fabric import Connection as FabricConnection
from paramiko.ssh_exception import SSHException


class DeviceConnection(Protocol):
    """DeviceConnection abstract base class"""

    def test_connection(self) -> bool:
        ...

    def fetch_backup(self) -> None:
        ...


class SshConnection(DeviceConnection):
    """DeviceConnection using Fabric"""

    def __init__(
        self, ip_address: str, username: str, connection_timeout: int, key_file: str
    ) -> None:
        self.ip_address = ip_address
        self.username = username
        self.connection_timeout = connection_timeout
        self.key_file = key_file

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
            except (TimeoutError, SSHException):
                return False

    def fetch_backup(self) -> None:
        with FabricConnection(
            host=self.ip_address,
            user=self.username,
            connect_timeout=self.connection_timeout,
            connect_kwargs={"key_filename": self.key_file},
        ) as connection:
            connection.run("/export file=backup", hide=True, warn=False)
            connection.get("backup.rsc", f"backups/backup_{self.ip_address}.rsc")
            connection.run("file/remove backup.rsc", hide=True, warn=False)
