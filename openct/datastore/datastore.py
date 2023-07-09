"""
Access persistent data.
"""
from abc import ABC, abstractmethod

import yaml


class Datastore(ABC):
    """Datastore ABC."""

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def get_next_item(self):
        pass

    @abstractmethod
    def get_number_of_items(self):
        pass


class Yaml(Datastore):
    """Using a YAML file as a datastore."""

    def __init__(self, file_path="datastore/datastore.yml"):
        self.file_path = file_path
        with open(self.file_path, "r", encoding="UTF8") as yaml_file:
            self.data = yaml.safe_load(yaml_file)
        self.data_generator = self._data_as_generator()

    def _data_as_generator(self):
        for item in self.data:
            yield item

    def get_next_item(self):
        try:
            return next(self.data_generator)
        except StopIteration:
            return

    def get_number_of_items(self):
        number_of_items = 3
        return number_of_items
