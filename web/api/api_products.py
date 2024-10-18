from ..models.product_model import Products
from ..config.db import connect
from sqlmodel import Session,select


def getAllProducts():
    engine= connect()
    with Session(engine) as session:
        query = select(Products)
        return session.exec(query).all()