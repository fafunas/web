from ..models.order_model import Order



#Funcion para armar los items que se reciben por el formulario
def cleanData(data={}):
    try:
        objects = [
            {'id': key.split('_')[1], 'quantity': int(value)}
            for key, value in data.items() if int(value) > 0
        ]
        newOrder=Order(total=2000,items=objects)
        return newOrder
    except BaseException as be:
        print(be)
        return []


