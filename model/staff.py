from .item import Item

# Staff inherits id and name from Item, and adds role
class Staff(Item):
    def __init__(self, id=None, name=None, role=None):
        super().__init__(id, name)
        self._role = role

    # Getter and setter for Role
    @property
    def role(self):
        return self._role

    @role.setter
    def role(self, value):
        self._role = value

    # Converts staff data to a CSV line format for saving
    def to_csv(self):
        return f"{self.id},{self.name},{self.role}\n"

    # Friendly text representation of staff details
    def __str__(self):
        return f"Staff ID: {self.id} | Name: {self.name} ({self.role})"
