from fastapi import FastAPI
from database import Base, engine
from routers import products
from models.product import Product


Base.metadata.create_all(bind=engine)



app=FastAPI(title="POS API", version="1")
app.include_router(products.router)
