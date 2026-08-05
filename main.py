from dotenv import load_dotenv
load_dotenv()
from fastapi import FastAPI
from database import Base, engine


from app.models.category import Category
from app.models.customer import Customer
from app.models.product import Product
from app.models.payment import Payment
from app.models.receipt import Receipt
from app.models.sale_item import SaleItem
from app.models.sale import Sale
from app.models.supplier import Supplier
from app.models.user import User


Base.metadata.drop_all(bind=engine)

Base.metadata.create_all(bind=engine)

from app.routers import ( 
    category,
    customer,
    payment,
    product,
    receipt,
    sale_item,
    sale,
    supplier,
    user,
)

app = FastAPI(title="POS API", version="1")

app.include_router(category.router)
app.include_router(product.router)
app.include_router(customer.router)
app.include_router(payment.router)
app.include_router(receipt.router)
app.include_router(sale_item.router)
app.include_router(sale.router)
app.include_router(supplier.router)
app.include_router(user.router)
