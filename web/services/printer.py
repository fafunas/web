
import textwrap
from datetime import datetime
import base64
from ..models.order_model import Order


def print_thermal_ticket(item: Order, obs: str) -> str:
    try:
        # Crear el contenido del ticket como un string
        ticket_lines = []

        # Comando ESC POS para texto grande (doble altura y doble ancho)
        esc_pos_double_size = "\x1b!\x30"

        # Encabezado del ticket (número de ticket centrado y grande)
        ticket_lines.append(esc_pos_double_size)
        ticket_lines.append(f"{item.nro_order}".center(40, " "))
        ticket_lines.append("\x1b!\x00")  # Volver al tamaño normal
        ticket_lines.append("=" * 40)

        # Fecha del ticket
        formatted_date = item.created_at.strftime("%d/%m/%Y %H:%M:%S") if isinstance(item.created_at, datetime) else str(item.created_at)
        ticket_lines.append(f"Fecha: {formatted_date}")
        ticket_lines.append("-" * 40)

        # Productos
        ticket_lines.append("Productos:")
        for producto in item.productos:
            product_text = f"{producto.name} - Cantidad: {producto.quantity}"
            ticket_lines.append(product_text)

        ticket_lines.append("-" * 40)

        # Observaciones
        ticket_lines.append("Observaciones:")
        wrapped_obs = textwrap.wrap(obs, width=38)  # Ajustar ancho para impresión
        ticket_lines.extend(wrapped_obs)

        ticket_lines.append("=" * 40)

        # Feed del papel al final (3 líneas en blanco usando ESC POS)
        ticket_lines.append("\n\n\n\x1b\x64\x03")

        # Combinar todas las líneas en un solo string con saltos de línea
        ticket_content = "\n".join(ticket_lines)

        # Convertir el contenido del ticket a base64
        ticket_base64 = base64.b64encode(ticket_content.encode("utf-8")).decode("utf-8")

        return ticket_base64
    except Exception as error:
        print(f"Error al generar el ticket: {error}")
        return ""