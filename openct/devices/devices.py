"""Module for device classes"""

from abc import ABC, abstractmethod

from openct.connections import DeviceConnection, SshConnection
from openct.setup import Config


class Device(ABC):
    """Device abstract base class"""

    def __init__(self, connection: DeviceConnection) -> None:
        self.connection = connection

    @abstractmethod
    def fetch_backup(self) -> str:
        ...

    def is_available(self) -> bool:
        return self.connection.test_connection()


class RouterOSDevice(Device):
    """RouterOS device"""

    def __init__(self, ip_address: str, config: Config) -> None:
        super().__init__(SshConnection(ip_address, config))

    def fetch_backup(self) -> str:
        self.connection.run_command("/export file=backup")
        self.connection.get_backup("backup.rsc", ".rsc")
        self.connection.run_command("file/remove backup.rsc")


class PfSenseDevice(Device):
    """PfSense device"""

    def __init__(self, ip_address: str, config: Config) -> None:
        super().__init__(SshConnection(ip_address, config))

    def fetch_backup(self) -> None:
        self.connection.get_backup("/cf/conf/config.xml", ".xml")
