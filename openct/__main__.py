"""Main entry point for the OpenCT application."""

import logging

from tqdm import tqdm

from openct.setup import setup_config, Config
from openct.datastore import Datastore, get_datastore
from openct.devices import RouterOSDevice


config: Config = setup_config()

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
            config.dirs.backup_dir,
        )

        if device.is_available():
            device.fetch_backup()
        else:
            logging.error("Could not connect to device %s", host)
