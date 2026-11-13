from .item import Item

# Product, the finished goods made in the factory (like, Dining Chair, Table)
class Product(Item):
    def __init__(self, id=None, name=None, stock_qty=0, unit_price=0.0):
        super().__init__(id, name)
        self._stock_qty = int(stock_qty) if stock_qty is not None else 0
        self._unit_price = float(unit_price) if unit_price is not None else 0.0

    # Number of finished units in stock
    @property
    def stock_qty(self):
        return self._stock_qty

    @stock_qty.setter
    def stock_qty(self, value):
        self._stock_qty = int(value)

    # Selling price per finished unit in PHP
    @property
    def unit_price(self):
        return self._unit_price

    @unit_price.setter
    def unit_price(self, value):
        self._unit_price = float(value)

    # Format data for saving into products.csv
    def to_csv(self):
        return f"{self.id},{self.name},{self.stock_qty},{self.unit_price}\n"

    # Display format for printing finished products
    def __str__(self):
        return f"[{self.id}] {self.name} | Finished Stock: {self.stock_qty} pcs | Price: PHP {self.unit_price:.2f}"
