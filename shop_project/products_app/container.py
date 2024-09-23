from products_app.protocols.repositories.product import ProductRepository as ProductRepositoryProtocol
from dependency_injector.providers import Configuration, Factory
from dependency_injector.containers import DeclarativeContainer
from products_app.repositories.product import ProductRepository
from typing import Self


class Container(DeclarativeContainer):
    __instance = None

    def __new__(cls) -> Self:
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    config = Configuration()

    product_repository: ProductRepositoryProtocol = Factory(ProductRepository)
