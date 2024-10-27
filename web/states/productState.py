import reflex as rx
from ..models.product_model import Products
from ..services.productServices import getAllProductsServices,createProductService,updateProductService,deleteProductServices
from typing import List



class ProductState(rx.State):
    products: list[Products] = []
    error: str = ""
    
    @rx.background
    async def get_all_products(self): #Recupero los productos y los meto en una variable en el estado
        async with self:
            self.products = getAllProductsServices()
            
            
    
    @rx.background
    async def createProduct(self, data={}): #Este data viene del formulario
        async with self:
            try:
                createProductService(data)
                self.products = getAllProductsServices() #Deberia recargar la lista products y actualizar la tabla
            except BaseException as be:
                self.error = be
                print(be)
                
    @rx.background
    async def updateProduct(self,data={}):
        async with self:
            try:
                updateProductService(data)
                self.products = getAllProductsServices()
            except BaseException as be:
                print(be)   
                
    @rx.background
    async def deleteProduct(self,data={}):
        async with self:
            try:
                deleteProductServices(data)
                self.products = getAllProductsServices()
            except BaseException as be:
                print(be) 