from .item import Item

# RawMaterial, the ingredients/parts used in production (like Wood, Screws)
class RawMaterial(Item):
    def __init__(self, id=None, name=None, unit=None, stock_qty=0.0, unit_cost=0.0):
        super().__init__(id, name)
        self._unit = unit
        self._stock_qty = float(stock_qty) if stock_qty is not None else 0.0
        self._unit_cost = float(unit_cost) if unit_cost is not None else 0.0

    # Unit of measurement
    def unit(self):
        return self._unit

    @unit.setter
    def unit(self, value):
        self._unit = value

    # Available stock quantity
    @property
    def stock_qty(self):
        return self._stock_qty

    @stock_qty.setter
    def stock_qty(self, value):
        self._stock_qty = float(value)

    # Cost per unit in PHP
    @property
    def unit_cost(self):
        return self._unit_cost

    @unit_cost.setter
    def unit_cost(self, value):
        self._unit_cost = float(value)

    # Format data for saving into materials.csv
    def to_csv(self):
        return f"{self.id},{self.name},{self.unit},{self.stock_qty},{self.unit_cost}\n"

    # Display format for printing in the console
    def __str__(self):
        return f"[{self.id}] {self.name} | Stock: {self.stock_qty} {self.unit} | Unit Cost: PHP {self.unit_cost:.2f}"
