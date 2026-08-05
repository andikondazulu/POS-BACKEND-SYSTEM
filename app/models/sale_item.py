from sqlalchemy import(
    String,
    Column,
    Integer,
    DECIMAL,
    ForeignKey
)
import uuid
from sqlalchemy.orm import relationship
from database import Base

class SaleItem(Base):
    __tablename__= "sale_items"
    
    
    sale_item_id= Column(String(50), primary_key=True, default=lambda: str(uuid.uuid4()), autoincrement=False)
    sale_id= Column(String(50), ForeignKey("sales.sale_id"), nullable=True)
    product_id= Column(String(50), ForeignKey("products.product_id"), nullable=True)
    quantity=Column(Integer, nullable=False)
    unit_price= Column(DECIMAL(10,2), nullable=False)
    discount_amount= Column(DECIMAL(10,2), nullable=True)
    total_price=Column(DECIMAL(10,2), nullable=False)
    
    
    sale=relationship("Sale", back_populates="sales")
    product=relationship("Product", back_populates="products")
    
    