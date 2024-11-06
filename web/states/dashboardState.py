import reflex as rx
from ..services.shiftServices import startShiftServices, endShiftServices,checkOpenShiftStatusService, getUnfinishdOrders
from ..services.productServices import getAllProductsServices
from ..services.orderServices import cleanData, createOrderServices,getAllOrdersServices, updateFinishtime, getDataCard
from ..models.product_model import Products
from ..models.dashboardModel import OrderType


class DashboardState(rx.State):
    shift_status:bool 
    products: list[Products] = []
    orderTable: list[OrderType] = []
    order_data: dict = {}
    openedDialog: bool = False
    productconfirm: list[dict]=[]
    statusCards: dict={}
    
    def closeDialog(self):
        self.openedDialog=False
    
        
    def handle_submit(self,data={}):
        items=cleanData(data)
        self.productconfirm = items.productos
        self.order_data=items
        self.openedDialog = True
        
    @rx.background
    async def createOrder(self):
        async with self:
            createOrderServices(self.order_data)
            self.openedDialog = False
            self.orderTable= getAllOrdersServices()
            self.statusCards = getDataCard()
            
    
    @rx.background
    async def startShift(self):
        async with self:
            startShiftServices()
            self.shift_status= True
            self.statusCards = getDataCard()
    
    
    @rx.background
    async def closeShift(self):
        async with self:
            endShiftServices()
            #print(getUnfinishdOrders())
            self.shift_status=False
            #self.statusCards = getDataCard()
   
            
    @rx.background
    async def on_load(self):
        async with self:
            self.shift_status= checkOpenShiftStatusService()
            self.products= getAllProductsServices()
            self.orderTable= getAllOrdersServices()
            self.statusCards = getDataCard()
            
    @rx.background
    async def UpdateItem(self,id,field: str):
        async with self:
            updateFinishtime(id,field)
            self.orderTable= getAllOrdersServices()
            self.statusCards = getDataCard()
                
            