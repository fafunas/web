import reflex as rx
from ..models.dashboardModel import OrderType
from ..services.reportServcices import getAllOrdersServices


class ReportState(rx.State):
    data : list[OrderType]=[]
    
    
    
    
    @rx.background
    async def onload(self):
        async with self:
            self.data=getAllOrdersServices()
           # print(self.data)
        