"""
Access persistent data.
"""
from abc import ABC, abstractmethod

import yaml


class Datastore(ABC):
    """
    Datastore ABC.
    """

    @abstractmethod
    def __init__(self):
        ...

    @abstractmethod
    def get_data(self):
        ...

    @abstractmethod
    def make_pylint_happy(self):
        ...


class _Yaml(Datastore):
    """
    Using a YAML file as a datastore.
    """

    def __init__(self, file_path="datastore/datastore.yml"):
        self.file_path = file_path

    def get_data(self):
        with open(self.file_path, "r", encoding="UTF8") as yaml_file:
            data = yaml.safe_load(yaml_file)
        return data

    def make_pylint_happy(self):
        ...


class _SQLite(Datastore):
    """
    NOT IMPLEMENTED. Example only.
    Using a SQLite database as a datastore.
    """

    def __init__(self):
        ...

    def get_data(self):
        data = "These are not the data you are looking for."
        return data

    def make_pylint_happy(self):
        ...


def get_datastore(datastore_type="yaml") -> Datastore:
    """
    Datastore factory that returns the concrete class
    for the selected datastore.
    """
    datastore_types = {
        "yaml": _Yaml,
        "sqlite": _SQLite,
    }
    if datastore_type in datastore_types:
        return datastore_types[datastore_type]
    return None
