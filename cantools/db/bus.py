# A CAN bus.

class Bus(object):
    """A CAN bus.

    """

    def __init__(self,
                 name,
                 comment=None):
        self._name = name
        self._comment = comment

    @property
    def name(self):
        """The bus name as a string.

        """

        return self._name

    @property
    def comment(self):
        """The bus comment, or ``None`` if no comment is available.

        """

        return self._comment

    def __repr__(self):
        return "bus('{}', {})".format(
            self._name,
            "'" + self._comment + "'" if self._comment is not None else None)
