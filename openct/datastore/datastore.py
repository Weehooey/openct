"""
Access persistent data.
"""
from abc import ABC, abstractmethod


class Datastore(ABC):
    """Datastore ABC."""

    @abstractmethod
    def get_next_item(self):
        pass

    @abstractmethod
    def get_number_of_items(self):
        pass

class Yaml(Datastore):
    """Using a YAML file as a datastore."""

    def __init__(self):
        pass

    def get_next_item(self):
        next_item = "something"
        return next_item

    def get_number_of_items(self):
        number_of_items = 3
        return number_of_items
    
    