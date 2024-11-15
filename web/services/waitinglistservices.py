def getNumOrdersServices(items)->list:
    prep=[]
    retirar=[]
    #print(items)
    for item in items:
        if item['finish_time'] is not None:
            retirar.append(item['orders_num'])
        else:
            prep.append(item['orders_num'])
    return [prep,retirar]

    
    