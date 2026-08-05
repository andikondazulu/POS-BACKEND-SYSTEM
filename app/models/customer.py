from sqlalchemy.sql import func
from sqlalchemy import(
    Integer, 
    Column,
    String,
    Boolean,
    DateTime 
)

from database import Base
import uuid

class Customer(Base):
    
    __tablename__="customers"
    

    customer_id = Column(String(50), primary_key=True, default= lambda: str (uuid.uuid4()), autoincrement=False)
    first_name=Column(String(100), nullable=False)
    last_name=Column(String(100), nullable=False)
    phone_no=Column(String(20), nullable= True)
    address=Column(String(50), nullable=True)
    is_active=Column(Boolean, nullable=False, default=True)
    created_at=Column(DateTime(timezone=True), server_default=func.now())
    updated_at=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())
    
     