from sqlalchemy import (
    Boolean, 
    Column,
    DateTime,
    ForeignKey, 
    Integer,
    Numeric, 
    String
)

from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from database import Base

class Product(Base):
    __table__= "products"
    
    id= Column(Integer, primary_key=True, index=True)
    name=Column(String, nullable=False)
    price=Column(Numeric(10,2), nullable=False)
    cost=Column(Numeric(10,2), nullable=True)
    quantity= Column(Integer,nullable=False)
    category_id= Column(Integer, ForeignKey("categories.id"), nullable=True)
    supplier_id= Column(Integer, ForeignKey("suppliers.id"), nullable=True)
    barcode= Column(String, nullable=True)
    is_active=Column(Boolean, nullable=False, default=True)
    created_at=Column(DateTime(timezone=True), server_default=func.now)
    
    category=relationship("Category", back_populates="products")
    supplier=relationship("Supplier", back_populates="products")
    inventory=relationship(
        "Inventory", back_populates="prodcuts", uselist=False
    )
    