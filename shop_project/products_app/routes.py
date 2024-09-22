from products_app.views import handle_products
from django.urls import path

urlpatterns = [
    path("products", handle_products),
]
