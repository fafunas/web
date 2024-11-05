#Al recibir un prodcuto devolvere un dict para trabajarlo
def shift_schema(shift)-> dict:
    return {
        "id" : str(shift["_id"]),
        "start_time": shift["start_time"],
        "shift_num": shift["shift_num"],
        "end_time": shift["end_time"],
        "status": shift["status"],
        "orders": shift["orders"]
    }
    
#Recibo varios productos y devuelvo una lista de todo    
def shifts_schema(shifts)-> list:
    return [shift_schema(shift) for shift in shifts]

