"""Main entry point for the OpenCT application."""

import os
import time
import logging

from tqdm import tqdm

from openct.config import Config, load_config
from openct.datastore import Datastore, get_datastore
from openct.devices import RouterOSDevice

config: Config = load_config()

log_file = os.path.join(
    config.dirs.log_dir, f"ocb_{time.strftime('%Y%m%d_%H%M%S')}.log"
)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(module)s] [%(levelname)s] %(message)s",
    filename=log_file,
    filemode="a",
    encoding="utf-8",
)

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
