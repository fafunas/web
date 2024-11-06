from datetime import datetime


def reportSchema(order)->dict: #Usamos este esquema solo para visualizar la tabla principal
    return{
        "created_at":time(order["created_at"]),
        "shift":order["shift_num"],
        "order": order["nro_order"],
        "name": order["name"],
        "quantity": order["quantity"],
        "price" : f"${order["precio_unitario"]}",
        "total": f"${order["total"]}",
              
    }
    
def time(item:datetime):
    return item.strftime('%Y-%m-%d %H:%M')
    
def reports_schema(orders)-> list:
    return [reportSchema(order) for order in orders]
