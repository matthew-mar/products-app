from products_app.protocols.repositories.product import ProductRepository
from products_app.exceptions.external import ProductCreateException
from products_app.exceptions.internal import AlreadyExistException
from products_app.serializers.requests import ProductSerializer
from rest_framework.pagination import LimitOffsetPagination
from dependency_injector.wiring import inject, Provide
from rest_framework.decorators import api_view
from rest_framework.response import Response
from products_app.container import Container
from rest_framework.request import Request


@api_view(http_method_names=["GET", "POST"])
def handle_products(request: Request) -> Response:
    match request.method:
        case "GET":
            return get_products(request)
        case "POST":
            return create_product(request)


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



class ProductPaginator(LimitOffsetPagination):
    default_limit = 1
    offset = 0


@inject
def get_products(
    request: Request,
    product_repo: ProductRepository = Provide[Container.product_repository]
) -> Response:
    products = product_repo.get_all()
    paginator = ProductPaginator()
    result_page = paginator.paginate_queryset(products, request)
    serializer = ProductSerializer(result_page, many=True)
    return paginator.get_paginated_response(serializer.data)
