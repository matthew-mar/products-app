from products_app.dto import ProductDTO, ProductKeys
from shop_project.validators import string

from rest_framework.serializers import (
    IntegerField,
    FloatField,
    Serializer,
    CharField,
)


class ProductSerializer(Serializer):
    id = IntegerField(required=False)
    name = CharField(
        allow_blank=False,
        min_length=3,
        max_length=50,
        validators=[string]
    )
    description = CharField(allow_blank=True, required=False)
    price = FloatField(min_value=1)

    def create(self, validated_data: ProductKeys) -> ProductDTO:
        return ProductDTO(**validated_data)
