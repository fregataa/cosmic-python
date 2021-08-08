
from datetime import date, timedelta

class OrderLine:

    def __init__(self, ref: str, sku: str, qty: int) -> None:
        self.ref = ref
        self.sku = sku
        self.qty = qty


class Batch:

    def __init__(self, ref: str, sku: str, qty: int, eta: date) -> None:
        self.ref = ref
        self.sku = sku
        self._available_quantity = qty
        self.eta = eta

    def allocate(self, line: OrderLine):
        self._available_quantity -= line.qty

    @property
    def available_quantity(self):
        return self._available_quantity
