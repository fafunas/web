##Validaciones

from ..api.api_products import getAllProducts, createProduct, getProductbyName, deleteProduct, updateProduct
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
    
def deleteProductservice(id:int):
    return deleteProduct(id=id)

def updateProductService(id:int,name:str, price:int):
    try:
        updateProd = Products(name=name,price=price)#Convierto al obj del modelo
    # print(updateProd,id)
        return updateProduct(id,updateProd)
    except:
        raise BaseException("El usuario ya existe")
        