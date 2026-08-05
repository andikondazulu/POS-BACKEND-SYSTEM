from sqlalchemy.sql import func
from sqlalchemy import(
    Column,
    String,
    Boolean,
    DateTime, 
)

from database import Base
import uuid

class Supplier(Base):
    
    __tablename__="suppliers"
    

    supplier_id = Column(String(50), primary_key=True, default= lambda: str (uuid.uuid4()), autoincrement=False)
    company_name=Column(String(50), nullable=False)
    contact_name=Column(String(50), nullable=False)
    email=Column(String(50), unique=True, nullable=False)
    supplier_phone=Column(String(20), unique=True, nullable= False)
    address=Column(String(50), nullable=True)
    is_active=Column(Boolean, nullable=False, default=True)
    created_at=Column(DateTime(timezone=True), server_default=func.now())
    
     