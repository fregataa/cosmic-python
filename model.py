from dataclasses import dataclass
from datetime import date, timedelta
from typing import Optional

@dataclass(frozen=True)
class OrderLine:
    orderid: str
    sku: str
    qty: int

class Batch:

    def __init__(self, ref: str, sku: str, qty: int, eta: Optional[date]) -> None:
        self.reference = ref
        self.sku = sku
        self._available_quantity = qty
        self.eta = eta

    def can_allocate(self, line: OrderLine):
        return self.sku == line.sku and self._available_quantity >= line.qty

    def allocate(self, line: OrderLine):
        self._available_quantity -= line.qty
    
    def deallocate(self, line: OrderLine):
        pass

    @property
    def available_quantity(self):
        return self._available_quantity
