from sqlalchemy import(
    String,
    Column, 
    ForeignKey,
    DateTime,
    DECIMAL, 
    Enum
)
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from database import Base
import uuid
import enum

class SalesStatus(str, enum.Enum):
    COMPLETED = "completed"
    CANCELLED = "cancelled"
    REFUNDED = "refunded"



class Sale(Base):
    __tablename__="sales"
    
    sale_id=Column(String(50), primary_key=True, default=lambda:str(uuid.uuid4()), autoincrement=False)
    customer_id=Column(String(50), ForeignKey("customers.customer_id"), nullable=True)
    user_id= Column(String(50), ForeignKey("users.user_id"), nullable=True)
    sale_date=Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    subtotal=Column(DECIMAL(10,2), nullable=False)
    tax_amount=Column(DECIMAL(10,2), nullable=False)
    discount_amount=Column(DECIMAL(10,2), nullable=True)
    total_amount=Column(DECIMAL(10,2), nullable=False)
    status=Column(Enum(SalesStatus, name="sale_satus_enum"), nullable=False)
    
    
    user=relationship("User", back_populates="users")
    customer=relationship("Customer", back_populates="customers")
    receipt = relationship("Receipt", back_populates="sale", uselist=False)   
    