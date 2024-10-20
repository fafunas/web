from ..models.product_model import Products
from ..config.db import connect
from sqlmodel import Session,select

# aca creariamos todas las queries para la bd
def getAllProducts():
    engine= connect()
    with Session(engine) as session:
        query = select(Products)
        return session.exec(query).all()
    
def createProduct(product:Products):
    engine= connect()
    with Session(engine) as session:
        session.add(product)
        session.commit()
        query = select(Products)
        return session.exec(query).all()
    
    
def getProductbyName(product:str):
    engine= connect()
    with Session(engine) as session:
        query= select(Products).where(Products.name==product)
        return session.exec(query).all()
    
    
