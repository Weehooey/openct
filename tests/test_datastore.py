"""Tests for the Datastore class."""

from openct.datastore.datastore import Yaml

def test_get_next_item():
    """Test this function."""
    dstore = Yaml()
    item_returned = dstore.get_next_item()
    assert item_returned

def test_get_number_of_items():
    """Get number of items in datastore should return an int."""
    dstore = Yaml()
    returned_value = dstore.get_number_of_items()
    assert isinstance(returned_value, int)
    