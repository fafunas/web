import win32print
import win32ui
import win32con
import textwrap
from ..models.order_model import Order

def print_thermal_ticket(item: Order, obs: str):
   try:
       # Obtener nombre de impresora predeterminada
       printer_name = win32print.GetDefaultPrinter()
       hPrinter = win32print.OpenPrinter(printer_name)

       # Iniciar trabajo de impresión
       hDC = win32ui.CreateDC()
       hDC.CreatePrinterDC(printer_name)

       try:
           hDC.StartDoc("Ticket Térmico")
           hDC.StartPage()

           # Configurar fuentes
           # Fuente para número de ticket (grande)
           ticket_number_font = win32ui.CreateFont({
               "name": "Segoe UI",
               "height": 160,
               "weight": win32con.FW_BOLD,
               
           })

           # Fuente para texto normal
           normal_font = win32ui.CreateFont({
               "name": "Segoe UI",
               "height": 35,
               "weight": win32con.FW_NORMAL,
               
           })

           # Calcular posiciones
           y = 20
           x = 50
           line_height = 45
           printer_width = 580  # Ancho aproximado de impresora térmica

           # Imprimir número de ticket centrado y grande
           hDC.SelectObject(ticket_number_font)
           ticket_text = f"{item.nro_order}"
           text_width = hDC.GetTextExtent(ticket_text)[0]
           centered_x = (printer_width - text_width) // 2
           hDC.TextOut(centered_x, y, ticket_text)
           y += 170
           
           # Cambiar a fuente normal
           hDC.SelectObject(normal_font)

           # Imprimir fecha
           hDC.TextOut(x, y, f"Fecha: {item.created_at}")
           y += line_height

           # Imprimir productos
           hDC.TextOut(x, y, "Productos:")
           y += line_height
           for producto in item.productos:
               product_text = f"{producto.name} - Cantidad: {producto.quantity}"
               hDC.TextOut(x + 50, y, product_text)
               y += line_height

           # Imprimir observaciones con wrap
           hDC.TextOut(x, y, "Observaciones:")
           y += line_height
           
           # Dividir observaciones en líneas
           wrapped_obs = textwrap.wrap(obs, width=40)
           for obs_line in wrapped_obs:
               hDC.TextOut(x + 50, y, obs_line)
               y += line_height

           win32print.StartDocPrinter(hPrinter, 1, ("Ticket", None, "RAW"))
           win32print.WritePrinter(hPrinter, b"\x1B\x64\x03")
           win32print.WritePrinter(hPrinter, b"\x1B\x64\x03")
           win32print.WritePrinter(hPrinter, b"\x1D\x56\x01")

           # Finalizar impresión
           hDC.EndPage()
           hDC.EndDoc()

       except Exception as print_error:
           print(f"Error durante la impresión: {print_error}")

       finally:
           # Cerrar impresora
           win32print.ClosePrinter(hPrinter)

   except Exception as main_error:
       print(f"Error general: {main_error}")