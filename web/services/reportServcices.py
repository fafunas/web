from ..config.db import db_client
from ..schemas.order_schema import orders_schema

def getAllOrdersServices():
    query = [
    {
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