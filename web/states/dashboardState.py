import reflex as rx
from ..services.shiftServices import startShiftServices, getAllShiftsServices,endShiftServices,checkOpenShiftStatusService
from ..services.productServices import getAllProductsServices
from ..services.orderServices import cleanData, createOrderServices,getAllOrdersServices
from ..models.product_model import Products


class DashboardState(rx.State):
    shift_status:bool 
    products: list[Products] = []
    oderTable: list =[{}]
    order_data: dict = {}
    openedDialog: bool = False
    productconfirm: list[dict]=[]
    
    def closeDialog(self):
        self.openedDialog=False
    
        
    def handle_submit(self,data={}):
        items=cleanData(data)
        self.productconfirm = items.productos
        self.order_data=items
        self.openedDialog = True
        
    @rx.background
    async def getallOrders(self):
        async with self:
            print( getAllOrdersServices())
            #print(self.oderTable)
            
            
        
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
   
        