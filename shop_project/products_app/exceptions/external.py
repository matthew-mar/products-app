from rest_framework.exceptions import APIException


class ProductCreateException(APIException):
    status_code = 400
