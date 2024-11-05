def orderSchema(order)->dict: #Usamos este esquema solo para visualizar la tabla principal
    return{
        "id" : str(order["_id"]),
        "orders_num":order["nro_order"],
        "total": order["total"],
        "shift": order["shift_num"][0],
        "created_at": order["created_at"],
        "finish_time" : order["finish_time"],
        "pickUp_time": order["pickUp_time"],
        "productos": process_products(order["productos"])      
    }
    

def cardStatusSchema(order)->dict:
    try:
        neworder= list(order)
        return neworder[0]
    except:
        return {}

    
def process_products(productos):
    return [{key: value for key, value in producto.items() if key != 'product'} for producto in productos]
        
    
def orders_schema(orders)-> list:
    return [orderSchema(order) for order in orders]