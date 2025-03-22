from ..config.db import db_client
from ..schemas.reportSchema import reports_schema
from datetime import datetime,UTC,timedelta
import pandas as pd
import reflex as rx
import os

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
            'shift_num': '$shift_num',
            'payment': '$payment'
        }
    }
]
    
    try:
        orders = reports_schema(db_client.orders.aggregate(query))
        print(orders)
    except BaseException as be:
        print(be)
    return orders



def export_orders_to_excel(data, output_file='ordenes_reporte.xlsx'):
    """
    Exporta los datos de órdenes a un archivo Excel en la carpeta assets con formato.
    
    Args:
        data (list): Lista de diccionarios con los datos de las órdenes
        output_file (str): Nombre del archivo Excel de salida (default: 'ordenes_reporte.xlsx')
    """
    # Asegurarse de que el archivo se guarda en la carpeta `assets`
    assets_path = rx.get_upload_dir()
    if not os.path.exists(assets_path):
        os.makedirs(assets_path)
    output_file_path = os.path.join(assets_path, output_file)

    # Convertir la lista de diccionarios a DataFrame
    df = pd.DataFrame(data)
    
    # Convertir la columna created_at a datetime
    df['created_at'] = pd.to_datetime(df['created_at'])
    
    # Convertir las columnas de precio y total a números, removiendo el símbolo '$'
    df['price'] = df['price'].str.replace('$', '').str.replace(',', '').astype(float)
    df['total'] = df['total'].str.replace('$', '').str.replace(',', '').astype(float)
    
    # Crear un archivo Excel con ExcelWriter para poder dar formato
    with pd.ExcelWriter(output_file_path, engine='xlsxwriter') as writer:
        # Guardar el DataFrame en la hoja 'Ordenes'
        df.to_excel(writer, sheet_name='Ordenes', index=False)
        
        # Obtener el libro de trabajo y la hoja para dar formato
        workbook = writer.book
        worksheet = writer.sheets['Ordenes']
        
        # Definir formatos
        formato_fecha = workbook.add_format({
            'num_format': 'yyyy-mm-dd hh:mm',
            'align': 'center'
        })
        
        formato_numero = workbook.add_format({
            'num_format': '$#,##0.00',
            'align': 'right'
        })
        
        formato_header = workbook.add_format({
            'bold': True,
            'bg_color': '#D8E4BC',
            'border': 1,
            'align': 'center'
        })
        
        # Aplicar formatos a las columnas
        worksheet.set_column('A:A', 18, formato_fecha)  # created_at
        worksheet.set_column('B:B', 8)   # shift
        worksheet.set_column('C:C', 8)   # order
        worksheet.set_column('D:D', 15)  # name
        worksheet.set_column('E:E', 10)  # quantity
        worksheet.set_column('F:G', 12, formato_numero)  # price y total
        worksheet.set_column('H:H', 15)  # payment
        
        # Aplicar formato al encabezado
        for col_num, value in enumerate(df.columns.values):
            worksheet.write(0, col_num, value, formato_header)
        
        # Agregar filtros
        worksheet.autofilter(0, 0, len(df), len(df.columns) - 1)

    return output_file_path