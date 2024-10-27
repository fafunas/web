import reflex as rx
from ..services.shiftServices import startShiftServices, getAllShiftsServices,endShiftServices,checkOpenShiftStatusService


class DashboardState(rx.State):
    shift_status:bool 
    
    
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
        