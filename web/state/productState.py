"""import reflex as rx
from ..models.product_model import Product
from ..api.api_products import addProducts

class ProductState(rx.State):
    product : Product = Product()
    
    
    # Método para manejar el envío del formulario
    async def handle_submit(self, form_data: dict):
        # Verifica que los campos estén en el formulario
        name = form_data.get("name")
        price = form_data.get("price")
        
        # Asegúrate de que los campos están presentes
        if not name or not price:
            print("Faltan datos del formulario")
            return
        
        # Actualiza los valores del producto
        self.product.name = name
        self.product.price = int(price)  # Convierte el precio a entero
        print(f"Producto enviado: {self.product}")
        await addProducts(self.product)
        """
import reflex as rx
from ..models.product_model import Products
from ..api.api_products import getAllProducts

class ProductState(rx.State):
    products: list[Products] = []
    
    @rx.background
    async def get_all_products(self):
        async with self:
            self.products = getAllProducts()