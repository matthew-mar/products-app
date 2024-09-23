from rest_framework.serializers import ValidationError
from shop_project.checks import string as string_check


def string(value: str) -> None:
    if not string_check(value):
        raise ValidationError(f"'{value}' must be a valid string")
