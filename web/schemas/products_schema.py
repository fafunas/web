#Al recibir un prodcuto devolvere un dict para trabajarlo
def product_schema(product)-> dict:
    return {
        "id" : str(product["_id"]),
        "name": product["name"],
        "price": product["price"]
    }
    
#Recibo varios productos y devuelvo una lista de todo    
def products_schema(products)-> list:
    return [product_schema(product) for product in products]

