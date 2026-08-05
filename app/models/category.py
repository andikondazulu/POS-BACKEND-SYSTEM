from sqlalchemy import(
    String,
    Text,
    Boolean,
    Column
)
import uuid
from database import Base
from sqlalchemy.orm import relationship

class Category(Base):
    __tablename__="categories"
    
    category_id= Column(String(50), primary_key=True, default=lambda: str(uuid.uuid4()), autoincrement=False)
    name= Column(String(50), nullable=False)
    description= Column(Text, nullable=True)
    is_active=Column(Boolean,nullable=False, default= True)

    products = relationship("Product", back_populates="category")
    