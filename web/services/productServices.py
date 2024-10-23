##Validaciones
from ..config.db import db_client
from ..schemas.products_schema import products_schema



def getAllProducts():
    print("getAllProducts")
    product = db_client.products.find()
    return products_schema(product)


