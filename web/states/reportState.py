import reflex as rx
from ..services.reportServcices import getAllOrdersServices, export_orders_to_excel


class ReportState(rx.State):
    data : list[dict]=[]
    
    @rx.event(background=True)
    async def fillTable(self,datatime):
        async with self:
            self.data=getAllOrdersServices(datatime)
            export_orders_to_excel(self.data)
