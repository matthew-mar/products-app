from django.apps import AppConfig


class ProductsAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'products_app'

    def ready(self) -> None:
        from products_app.container import Container
        Container().wire(modules=["products_app.views"])        
