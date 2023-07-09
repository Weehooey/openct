"""Backup module."""

import os
import time
import logging

from tqdm import tqdm

from openct.config_loader import Config
from openct.devices import RouterOSDevice


def run_backup(config: Config, devices: list[str]) -> None:
    backup_dir = os.path.join(config.dirs.backup_dir, time.strftime("%Y%m%d_%H%M"))

    try:
        os.makedirs(backup_dir)
    except FileExistsError:
        pass

    with tqdm(total=100) as pbar:
        for host in devices:
            logging.info("Backing up device %s", host)
            pbar.update(100 / len(devices))
            device = RouterOSDevice(
                host,
                config.identity.username,
                config.settings.connection_timeout,
                config.identity.key_file,
            )
            if device.is_available():
                device.fetch_backup()
            else:
                logging.error("Could not connect to device")
