"""Tests for the Datastore class."""

from openct.datastore.datastore import Datastore as Ds

def test_get_next_item():
    """Test this function."""
    dstore = Ds()
    item_returned = dstore.get_next_item()
    assert item_returned
