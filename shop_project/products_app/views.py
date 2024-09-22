from products_app.protocols.repositories.product import ProductRepository
from products_app.exceptions.external import ProductCreateException
from products_app.exceptions.internal import AlreadyExistException
from products_app.serializers.requests import ProductSerializer
from dependency_injector.wiring import inject, Provide
from rest_framework.decorators import api_view
from rest_framework.response import Response
from products_app.container import Container
from rest_framework.request import Request


@api_view(http_method_names=["POST"])
@inject
def create_product(
    request: Request,
    product_repo: ProductRepository = Provide[Container.product_repository]
) -> Response:
    serializer = ProductSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    request_product = serializer.create(serializer.data)

    try:
        product = product_repo.create(request_product)
    except AlreadyExistException as e:
        raise ProductCreateException(detail=e.message)

    response = serializer.to_representation(product)
    return Response(data=response)
