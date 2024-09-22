from products_app.dto import ProductDTO
from typing import Protocol


class ProductRepository(Protocol):
    def create(self, product: ProductDTO) -> ProductDTO:
        ...
