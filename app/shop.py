from dataclasses import dataclass
from typing import List, Dict


@dataclass
class Shop:
    name: str
    location: List[float]
    products: Dict[str, float]

    def calculate_distance(self, customer_location: List[float]) -> float:
        return ((self.location[0] - customer_location[0]) ** 2
                + (self.location[1] - customer_location[1]) ** 2) ** 0.5

    def get_product_price(self, product: str) -> float | int:
        return self.products.get(product)
