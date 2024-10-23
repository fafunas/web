import reflex as rx
import asyncio
from ..models.product_model import Products
from ..services.productServices import getAllProducts
from typing import List



class ProductState(rx.State):
    products: list[Products] = []
    error: str = ""
    
    @rx.background
    async def get_all_products(self): #Recupero los productos y los meto en una variable en el estado
        async with self:
            self.products = getAllProducts()
            print(self.products)
            
  