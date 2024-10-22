from ..models.product_model import Products
from ..config.db import connect
from sqlmodel import Session,select

# aca creariamos todas las queries para la bd
def getAllProducts():
    engine= connect()
    with Session(engine) as session:
        query = select(Products)
        return session.exec(query).all()

#Crea producto nuevo   
def createProduct(product:Products):
    engine= connect()
    with Session(engine) as session:
        session.add(product)
        session.commit()
        query = select(Products)
        return session.exec(query).all()
    
#Recupera un producto por nombre   
def getProductbyName(product:str):
    engine= connect()
    with Session(engine) as session:
        query= select(Products).where(Products.name==product)
        return session.exec(query).all()
    

#Eliminar Producto

def deleteProduct(id:int):
    engine= connect()
    with Session(engine) as session:
        product= session.exec(select(Products).where(Products.id==id)).first()
        session.delete(product)
        session.commit()
        
    
#Actualziar Producto

def updateProduct(id:int, product:Products):
    engine=connect()
    with Session(engine) as session:
        updateProd = session.exec(select(Products).where(Products.id==id)).first()
        updateProd.name = product.name
        updateProd.price = product.price
        session.add(updateProd)
        session.commit()
        session.refresh(updateProd)
        

