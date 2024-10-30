import reflex as rx
from ..services.shiftServices import startShiftServices, getAllShiftsServices,endShiftServices,checkOpenShiftStatusService
from ..services.productServices import getAllProductsServices
from ..services.dashboardServices import cleanData
from ..models.product_model import Products


class DashboardState(rx.State):
    shift_status:bool 
    products: list[Products] = []
    order_data: dict = {}
    item_selected:str=""

    def set_value(self, value):
        self.value = value
        
    def handle_submit(self,data={}):
        items=cleanData(data)
       # items["ornder"]=1
        print(items)
    
    @rx.background
    async def startShift(self):
        async with self:
            startShiftServices()
            self.shift_status= True
    
    
    @rx.background
    async def closeShift(self):
        async with self:
            self.shift_status=False
            endShiftServices()
            
    @rx.background
    async def on_load(self):
        async with self:
            self.shift_status= checkOpenShiftStatusService()
            self.products= getAllProductsServices()
   
        