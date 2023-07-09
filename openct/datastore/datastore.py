"""
Access persistent data.
"""


class Datastore:
    """Datastore."""

    def __init__(self):
        self.fake = "fake"

    def get_next_item(self):
        """Return the next item from the datastore."""
        return None

    def do_nothing(self):
        """Do nothing."""
        print("Doing nothing")
