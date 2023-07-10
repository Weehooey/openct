"""Main entry point for the OpenCT application."""

import os
import time
import logging

from tqdm import tqdm

from logging_init import init_logger
from openct.config_loader import load_config
from openct.datastore import Yaml
from openct.config_loader import Config
from openct.devices import RouterOSDevice
from openct.datastore import Datastore


config: Config = load_config()

init_logger(config.dirs.log_dir)

backup_dir = os.path.join(config.dirs.backup_dir, time.strftime("%Y%m%d_%H%M"))

datastore: Datastore = Yaml()

with tqdm(total=100) as pbar:
    while host := datastore.get_next_item():
        logging.info("Backing up device %s", host)
        pbar.update(100 / datastore.get_number_of_items())

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
