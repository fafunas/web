from ..models.order_model import Order
from ..config.db import db_client
from bson import ObjectId
from ..services.shiftServices import lastShift


#Funcion para armar los items que se reciben por el formulario
def cleanData(data={}):
    try:
        # Crear un diccionario para almacenar los precios
        prices = {}
        names={}
        
        for key, value in data.items():
            if key.startswith('name'):
                id= key.split(".")[1]
                names[id]=value
            
            
        for key, value in data.items():
            if key.startswith('price_'):
                id = key.split('_')[1]
                prices[id] = float(value)

        # Crear los objetos con id, quantity y subtotal
        objects = []
        total = 0
        
        for key, value in data.items():
            if key.startswith('quantity_'):
                id = key.split('_')[1]
                quantity = int(value)
                if quantity > 0:
                    price = prices.get(id, 0) #Sino encuentra el ID retorna 0
                    name = names.get(id,0)
                    subtotal = price * quantity
                    total += subtotal
                    objects.append({
                        'product': ObjectId(id),
                        'quantity': quantity,
                        'price': price,
                        'name':name
                        #'subtotal': subtotal
                    })
        
        newOrder = Order(total=total, productos=objects)
        return newOrder
    except BaseException as be:
        print(be)
        
        return []
    


def createOrderServices(item:Order):
    shift = lastShift()
    item.shift_num=ObjectId(shift["_id"])
    newOrder = dict(item)
    del newOrder["id"]
    try:
        uid= db_client.orders.insert_one(newOrder).inserted_id
        print(f"Se ingreso correctamente con el id{uid}")
    except BaseException as be:
        print(be)
        
