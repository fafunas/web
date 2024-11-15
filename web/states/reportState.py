import reflex as rx
from ..models.dashboardModel import OrderType
from ..services.reportServcices import getAllOrdersServices


class ReportState(rx.State):
    data : list[dict]=[]
    
    @rx.event(background=True)
    async def fillTable(self,datatime):
        async with self:
            self.data=getAllOrdersServices(datatime)
            
        