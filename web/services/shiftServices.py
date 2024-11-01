from ..config.db import db_client
from ..models.shift_model import Shift
from ..models.shift_model import get_current_time
from datetime import datetime
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

def endShiftServices():
    last_shift= lastShift()
    endTime= get_current_time()
    uid=ObjectId(last_shift["_id"])
    print(uid)
    db_client.shifts.find_one_and_update({"_id":uid},{"$set":{"end_time":endTime,"status":False}})
    
    
def getAllShiftsServices():
        shifts= db_client.shifts.find()
        print(shifts_schema(shifts))
        
        #return shifts_schema(shifts)
        
def lastShift()->int:#Retorna el valor del ultimo turno
    last_shift = db_client.shifts.find_one(
            sort=[("shift_num", -1)]  # -1 para orden descendente
        )
    return last_shift

def checkOpenShiftStatusService()->bool:
    last = lastShift()
    return last["status"]


