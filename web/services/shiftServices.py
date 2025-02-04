from ..config.db import db_client
from ..models.shift_model import Shift
from ..models.shift_model import get_current_time
from ..schemas.shift_schema import shifts_schema
from bson import ObjectId



def startShiftServices():
    next_num = checkTotalShifts()
    new_shift = Shift(shift_num=next_num)
    shift_dict = dict(new_shift)
    del shift_dict["id"]
    #print(shift_dict)
    db_client.shifts.insert_one(shift_dict)

    
    
def checkTotalShifts()->int: #Tomo el ultimo shift y le suma uno para incrementar
    last_shift= lastShift()
    #print("Last Shifl",last_shift)
    return (last_shift["shift_num"] + 1) if last_shift else 1

#Actualiza el turno actual con el horario de finalizacion
def endShiftServices():
    if getUnfinishdOrders():
        last_shift= lastShift()
        endTime= get_current_time()
        uid=ObjectId(last_shift["_id"])
        print(uid)
        db_client.shifts.find_one_and_update({"_id":uid},{"$set":{"end_time":endTime,"status":False}})
    else:
        raise Exception("Quedan ordenes abiertas")
    
 #Retorna todos los documentos de turnos   
def getAllShiftsServices():
        shifts= db_client.shifts.find()
        print(shifts_schema(shifts))
        
        #return shifts_schema(shifts)


#Retorna el valor del ultimo turno        
def lastShift()->int:
    last_shift = db_client.shifts.find_one(
            sort=[("shift_num", -1)]  # -1 para orden descendente
        )
    return last_shift


#Retorna el status el ultimo shift
def checkOpenShiftStatusService()->bool:
    last = lastShift()
    return last["status"]

 #Funciona para ir incrementando el numero de ordenes por dia
def updateOrderNum():
    order = lastShift()
    uid= ObjectId(order["_id"])
    try:
        db_client.shifts.find_one_and_update({"_id":uid},{"$inc":{"orders":1}})
    except BaseException as be:
        print(be)

    
def getUnfinishdOrders()->bool:
    query=[
    {
        '$match': {
            'pickUp_time': None
        }
    }
    ]
    order=db_client.orders.aggregate(query)
    
    if any(order):
        return False
    else:
    # El cursor está vacío
        return True
    
    

