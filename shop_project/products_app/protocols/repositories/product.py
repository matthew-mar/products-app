from products_app.dto import ProductDTO
from typing import Protocol, Iterable


class ProductRepository(Protocol):
    def create(self, product: ProductDTO) -> ProductDTO:
        ...

    def get_all(self) -> Iterable[ProductDTO]:
        ...
