import reflex as rx
import json


class LocalState(rx.State):
    lsprep: str=rx.LocalStorage("{}",sync=True)
    lsret: str=rx.LocalStorage("{}",sync=True)
        
  
    @rx.event(background=True)
    async def getLsdata(self):
        async with self:
            self.prep = self.get_value(json.loads(self.lsprep))
            self.ready = self.get_value(json.loads(self.lsret))
            
    @rx.var(cache=True)
    def enprep(self)->list:
        return list(self.get_value(json.loads(self.lsprep)))
            
    @rx.var(cache=True)
    def ready(self)->list:
        return list(self.get_value(json.loads(self.lsret)))