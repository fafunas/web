import json
import websocket
import threading
import time

class WebSocketPrinter:
    def __init__(self, url="ws://127.0.0.1:12212/printer", on_connect=None, on_disconnect=None, on_update=None):
        self.url = url
        self.on_connect = on_connect or (lambda: None)
        self.on_disconnect = on_disconnect or (lambda: None)
        self.on_update = on_update or (lambda message: None)

        self.websocket = None
        self.connected = False
        self._reconnect_thread = None

        self.connect()

    def _on_message(self, ws, message):
        self.on_update(message)

    def _on_open(self, ws):
        self.connected = True
        self.on_connect()

    def _on_close(self, ws, close_status_code, close_msg):
        self.connected = False
        self.on_disconnect()
        self._reconnect()

    def connect(self):
        def run():
            self.websocket = websocket.WebSocketApp(
                self.url,
                on_message=self._on_message,
                on_open=self._on_open,
                on_close=self._on_close
            )
            self.websocket.run_forever()

        thread = threading.Thread(target=run, daemon=True)
        thread.start()

    def _reconnect(self):
        time.sleep(1)  # Esperar antes de reconectar
        self.connect()

    def submit(self, data):
        if not self.connected:
            raise ConnectionError("WebSocket no está conectado.")

        if isinstance(data, list):
            for element in data:
                self.websocket.send(json.dumps(element))
        else:
            self.websocket.send(json.dumps(data))

    def is_connected(self):
        return self.connected
    
def on_connect():
        print("Conectado al servidor WebSocket.")

def on_disconnect():
        print("Desconectado del servidor WebSocket.")

def on_update(message):
        print(f"Mensaje recibido: {message}")
    
    
print_service = WebSocketPrinter(
        url="ws://127.0.0.1:12212/printer",
        on_connect=on_connect,
        on_disconnect=on_disconnect,
        on_update=on_update
    )

def print_raw(base64):
        raw_content = base64
        print_service.submit({
            'type': 'RECEIPT',
            'raw_content': raw_content
        })
        print("Contenido enviado al servicio de impresión.")