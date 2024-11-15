import reflex as rx
from ..services.shiftServices import startShiftServices, endShiftServices,checkOpenShiftStatusService, getUnfinishdOrders
from ..services.productServices import getAllProductsServices
from ..services.orderServices import cleanData, createOrderServices,getAllOrdersServices, updateFinishtime, getDataCard
from ..services.waitinglistservices import getNumOrdersServices
from ..models.product_model import Products
from ..models.dashboardModel import OrderType
from ..states.LocalState import LocalState
import json


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
        
    async def waitingOrders(self):
        local_state = await self.get_state(LocalState)
        ordenes= getNumOrdersServices(self.orderTable)
        local_state.lsprep= json.dumps(ordenes[0])
        local_state.lsret= json.dumps(ordenes[1])
        
         
    @rx.event(background=True)
    async def createOrder(self):
        async with self:
            createOrderServices(self.order_data)
            self.openedDialog = False
            self.orderTable= await getAllOrdersServices()
            self.statusCards = getDataCard()
            await self.waitingOrders()
            
    
    @rx.event(background=True)
    async def startShift(self):
        async with self:
            startShiftServices()
            self.shift_status= True
            self.statusCards = getDataCard()
    
    
    @rx.event(background=True)
    async def closeShift(self):
        async with self:
            endShiftServices()
            self.shift_status=False
            return rx.clear_local_storage()
           
   
            
    @rx.event(background=True)
    async def on_load(self):
        async with self:
            self.shift_status= checkOpenShiftStatusService()
            self.products= getAllProductsServices()
            self.orderTable= await getAllOrdersServices()
            self.statusCards = getDataCard()
           
            
            
    @rx.event(background=True)
    async def UpdateItem(self,id,field: str):
        async with self:
            updateFinishtime(id,field)
            self.orderTable= await getAllOrdersServices()
            self.statusCards = getDataCard()
            await self.waitingOrders()
            
