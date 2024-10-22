import reflex as rx
import asyncio
from ..models.product_model import Products
from ..services.productServices import getProductsService,createProductService, deleteProductservice,updateProductService


class ProductState(rx.State):
    products: list[Products] = []
    error: str = ""
    
    @rx.background
    async def get_all_products(self): #Recupero los productos y los meto en una variable en el estado
        async with self:
            self.products = getProductsService()
            
    @rx.background
    async def createProduct(self, data={}):
        async with self:
            try:
                createProductService(name=data["name"],price=data["price"])
                self.products = getProductsService() #Deberia recargar la lista products y actualizar la tabla
            except BaseException as be:
                self.error = be
                print(be)
        #await self.handleNotification()

#Eliminar un producto de la tabla
    @rx.background
    async def deleteProduct(self, id:int):
        async with self:
            try:
                deleteProductservice(id)
                self.products = getProductsService()
            except BaseException as be:
                print(be)
                
    
    @rx.background
    async def updateProduct(self,data={}):
        async with self:
            try:
                print(data)
                updateProductService(id=data["id"],name=data["name"],price=data["price"])
                self.products = getProductsService() #Deberia recargar la lista products y actualizar la tabla
            except BaseException as be:
                self.error = be
                print(be)
    
    
    async def handleNotification(self):
        async with self:
            await asyncio.sleep(3)
            self.error=""       
            
    
    