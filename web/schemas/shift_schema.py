#Al recibir un prodcuto devolvere un dict para trabajarlo
def product_schema(shift)-> dict:
    return {
        "id" : str(shift["_id"]),
        "start_time": shift["start_time"],
        "end_time": shift["end_time"]
    }
    
#Recibo varios productos y devuelvo una lista de todo    
def products_schema(products)-> list:
    return [product_schema(product) for product in products]

