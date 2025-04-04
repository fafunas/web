from ..models.order_model import Order, get_current_time
from ..config.db import db_client
from bson import ObjectId
from ..schemas.order_schema import orders_schema, cardStatusSchema
from .shiftServices import lastShift, updateOrderNum


#Funcion para armar los items que se reciben por el formulario
def cleanData(data={})->Order:
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
        print("Error de cleand Data",be)
        
        return []
    
def deleteOrderServices(id):
    uid = ObjectId(id)
    try:
        db_client.orders.delete_one({"_id":uid})
        print("Se elimino correctamente")
    except BaseException as be:
        print("Error de Delete",be)

def createOrderServices(item:Order,obs:str,payment:str):
    shift = lastShift()
    item.observation=obs
    item.payment = payment
    nro_order = int(shift["orders"])
    item.shift_num=ObjectId(shift["_id"])
    item.nro_order= nro_order
    productdict= [
        {
            "quantity": producto.quantity, 
            "price": producto.price, 
            "name": producto.name,
            "product": producto.product
        } for producto in item.productos
    ]
    newOrder = dict(item)
    newOrder["productos"]=productdict
    del newOrder["id"]
    try:
        uid= db_client.orders.insert_one(newOrder).inserted_id
        print(f"Se ingreso correctamente con el id{uid}")
        updateOrderNum()# Si se agrega la order incremento
    except BaseException as be:
        print("Error de Create",be)
        

async def getAllOrdersServices():
    query = [
    {
        '$match': {
            'pickUp_time': None
        }
    }, {
        '$lookup': {
            'from': 'shifts', 
            'localField': 'shift_num', 
            'foreignField': '_id', 
            'as': 'shift_info'
        }
    }, {
        '$addFields': {
            'shift_num': '$shift_info.shift_num', 
            'shift_info': '$$REMOVE'
        }
    }
    ]
    
    orders = orders_schema(db_client.orders.aggregate(query))
    return orders

def updateFinishtime(id,field):
    uid = ObjectId(id)
    time = get_current_time()
    
    try:
        db_client.orders.find_one_and_update({"_id":uid},{"$set":{field:time}})
    except BaseException as be:
        print(be)
    
    
def getDataCard():
    shift = lastShift()
    actualShift= shift["shift_num"]
    
    query = [
    {
        '$lookup': {
            'from': 'shifts', 
            'localField': 'shift_num', 
            'foreignField': '_id', 
            'as': 'shift_info'
        }
    }, {
        '$match': {
            'shift_info.shift_num': actualShift
        }
    }, {
        '$group': {
            '_id': None, 
            'active': {
                '$sum': {
                    '$cond': [
                        {
                            '$and': [
                                {
                                    '$eq': [
                                        '$finish_time', None
                                    ]
                                }, {
                                    '$eq': [
                                        '$pickUp_time', None
                                    ]
                                }
                            ]
                        }, 1, 0
                    ]
                }
            }, 
            'ready': {
                '$sum': {
                    '$cond': [
                        {
                            '$and': [
                                {
                                    '$ne': [
                                        '$finish_time', None
                                    ]
                                }, {
                                    '$eq': [
                                        '$pickUp_time', None
                                    ]
                                }
                            ]
                        }, 1, 0
                    ]
                }
            }, 
            'total': {
                '$sum': {
                    '$cond': [
                        {
                            '$and': [
                                {
                                    '$ne': [
                                        '$created_at', None
                                    ]
                                }, {
                                    '$ne': [
                                        '$finish_time', None
                                    ]
                                }, {
                                    '$ne': [
                                        '$pickUp_time', None
                                    ]
                                }
                            ]
                        }, 1, 0
                    ]
                }
            }
        }
    }, {
        '$project': {
            '_id': 0, 
            'active': 1, 
            'ready': 1, 
            'total': 1
        }
    }
]
    
    cardsOrders = cardStatusSchema(db_client.orders.aggregate(query))
    return cardsOrders