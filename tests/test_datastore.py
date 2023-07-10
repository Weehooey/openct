"""Tests for the Datastore class."""

from openct.datastore.datastore import get_datastore


def test_data():
    """Test this function."""
    Dstore = get_datastore(datastore_type="yaml")
    dstore = Dstore(file_path="tests/data/test_datastore_001.yml")
    items_returned = dstore.get_data()
    assert items_returned[0] == "10.10.10.1"
    assert len(items_returned) == 5
