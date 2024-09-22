from products_app.views import create_product
from django.urls import path

urlpatterns = [
    path("products", create_product),
]
