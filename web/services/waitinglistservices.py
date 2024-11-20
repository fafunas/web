def getNumOrdersServices(items)->list:
    prep=[]
    retirar=[]
    #print(items)
    for item in items:
        if item['finish_time'] is not None:
            retirar.append(item['nro_order'])
        else:
            prep.append(item['nro_order'])
    return [prep,retirar]

    
    