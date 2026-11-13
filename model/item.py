
class Item:
    def __init__(self, id=None, name=None):
        self._id = id
        self._name = name

    # Getter and setter for ID
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    # Getter and setter for Name
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
