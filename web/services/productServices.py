##Validaciones

from ..api.api_products import getAllProducts, createProduct, getProductbyName
from ..models.product_model import Products


def getProductsService():
    product = getAllProducts()
    return product


def selectProductbyName(product:str):
    if(len(product)!=0):
        return getProductbyName(product)
    else:
        return getAllProducts()

def createProductService(name:str,price:int):
    product= getProductbyName(name)
    if (len(product)==0):
        new_product = Products(name=name,price=price)
        return createProduct(new_product)
    else:
        raise BaseException("El usuario ya existe")