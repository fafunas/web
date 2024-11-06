from ..config.db import db_client
from ..schemas.reportSchema import reports_schema
from datetime import datetime,UTC,timedelta

def getAllOrdersServices(dates):
    fromdate= datetime.strptime(dates["from"],'%Y-%m-%d').replace(tzinfo=UTC)
    todate= datetime.strptime(dates["to"],'%Y-%m-%d').replace(tzinfo=UTC)
    todate += timedelta(days=1)
   
    query = [
    {
        '$match': {
            'created_at': {
                '$gte': fromdate, 
                '$lt': todate
            }
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
            'shift_info': '$$REMOVE', 
            'finish_time': '$$REMOVE', 
            'pickUp_time': '$$REMOVE'
        }
    }, {
        '$unwind': '$productos'
    }, {
        '$unwind': '$shift_num'
    }, {
        '$project': {
            '_id': 0, 
            'quantity': '$productos.quantity', 
            'name': '$productos.name', 
            'precio_unitario': '$productos.price', 
            'total': {
                '$multiply': [
                    '$productos.quantity', '$productos.price'
                ]
            }, 
            'nro_order': '$nro_order', 
            'created_at': '$created_at', 
            'shift_num': '$shift_num'
        }
    }
]
    
    try:
        orders = reports_schema(db_client.orders.aggregate(query))
    except BaseException as be:
        print(be)
    return orders