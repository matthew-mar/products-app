from products_app.protocols.repositories.product import ProductRepository as ProductRepositoryProtocol
from products_app.exceptions.internal import AlreadyExistException
from products_app.dto import ProductDTO
from products_app.models import Product
from django.db import IntegrityError


class ProductRepository(ProductRepositoryProtocol):
    def create(self, product: ProductDTO) -> ProductDTO:
        try:
            return Product.objects.create(**product.dict)
        except IntegrityError as e:
            raise AlreadyExistException(e.args)
