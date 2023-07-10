"""Main entry point for the OpenCT application."""

import os
import time
import logging

from tqdm import tqdm

from logging_init import init_logger
from openct.config import Config, load_config
from openct.datastore import Datastore, get_datastore
from openct.devices import RouterOSDevice


config: Config = load_config()

init_logger(config.dirs.log_dir)

backup_dir = os.path.join(config.dirs.backup_dir, time.strftime("%Y%m%d_%H%M"))

Dstore = get_datastore(config.settings.datastore_type)
datastore: Datastore = Dstore()
devices = datastore.get_data()

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
