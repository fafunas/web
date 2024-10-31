import reflex as rx
from ..services.shiftServices import startShiftServices, getAllShiftsServices,endShiftServices,checkOpenShiftStatusService
from ..services.productServices import getAllProductsServices
from ..services.dashboardServices import cleanData, createOrderServices
from ..models.product_model import Products


class DashboardState(rx.State):
    shift_status:bool 
    products: list[Products] = []
    order_data: dict = {}
    openedDialog: bool = False
    productconfirm: list[dict]=[]
    
    def closeDialog(self):
        self.openedDialog=False
    
        
    def handle_submit(self,data={}):
        #print(data)
        items=cleanData(data)
        self.productconfirm = items.productos
        self.order_data=items
        print(self.productconfirm)
        #print(self.order_data)
        self.openedDialog = True
        
    @rx.background
    async def createOrder(self):
        async with self:
            createOrderServices(self.order_data)
            self.openedDialog = False
            
    
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
   
        