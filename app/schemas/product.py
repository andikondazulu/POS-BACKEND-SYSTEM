from datetime import datetime
from decimal import Decimal

from pydantic import BaseModel, ConfigDict

class ProductBase (BaseModel):
    name:str
    price:Decimal
    cost:Decimal | None=None
    quantity:int
    category_id: int | None=None
    supplier_id: int | None=None
    barcode: str | None=None
    is_active: bool | None=None

    
class ProductCreate (ProductBase):
    pass

class ProductUpdate(ProductBase):
    name:str | None=None
    price:Decimal |None=None
    cost:Decimal | None=None
    quantity:int | None=None
    category_id: int | None=None
    supplier_id: int | None=None
    barcode: str | None=None
    
class   ProductRead(ProductBase):
    model_config=ConfigDict(from_attributes=True)
    
    id:int
    created_at:datetime
    
    

    
    
   