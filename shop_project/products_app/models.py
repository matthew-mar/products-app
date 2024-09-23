from django.core.validators import MinLengthValidator
from django.db import models


class Product(models.Model):
    name = models.TextField(
        null=False, 
        max_length=50, 
        unique=True, 
        validators=[MinLengthValidator(3)]
    )
    description = models.TextField(null=True)
    price = models.FloatField(null=False)
