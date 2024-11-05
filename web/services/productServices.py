##Validaciones
from ..config.db import db_client
from ..schemas.products_schema import products_schema,product_schema
from bson import ObjectId
from ..models.product_model import Products



#Recupero todos los productos de la base
def getAllProductsServices():
    product = db_client.products.find()
    return products_schema(product)


#Crear nuevo registro

def createProductService(item):
    if type(findProduct(item))==Products:
        raise Exception("El producto ya existe")
    
    newProduct=Products(**item) #Hago esto para agregar el campo status
    product_dict= dict(newProduct)
    product_dict["name"]=product_dict["name"].capitalize()
    del product_dict["id"]
    
    uid= db_client.products.insert_one(product_dict).inserted_id
    print(f"Se ingreso correctamente con el id{uid}")
    getAllProductsServices()
    
#Actualiza un registro (En este caso solo actualizamos precio)    
def updateProductService(data={}):
    uid=data.pop("id") #Extraigo el ID de data
    updateProduct = db_client.products.update_one({"_id":ObjectId(uid)},{"$set":data}) #Debo convertir el uid a ObjectId para que Mongo lo reconozca y le paso el resto de data
    return updateProduct


#Funcion para recuperar un producto
def findProduct(data:dict):
    try:
        field, key = list(data.items())[0]  # Extrae el primer par clave-valor del diccionario
        query = {field: {"$regex": f"^{key}$", "$options": "i"}} #expresión regular insensible a mayúsculas
        product= db_client.products.find_one(query)
        return Products(**product)
    except:
        print("No se encuentra el producto")
        
#Eliminar producto

def deleteProductServices(data={}):
    uid= data.pop("id")
    deleteProduct = db_client.products.delete_one({"_id":ObjectId(uid)})
    return deleteProduct

