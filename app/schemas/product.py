from datetime import datetime
from decimal import Decimal


from pydantic import BaseModel, ConfigDict

class ProductBase (BaseModel):
    name:str
    price:Decimal
    quantity:int
    category_id: int | None=None
    supplier_id: int | None=None
    barcode: str | None=None
    is_active: bool | None=None
    
class ProductCreate (ProductBase):
    pass

class ProductUpdate(BaseModel):
    name:str | None=None
    price:Decimal |None=None
    quantity:int | None=None
    category_id: int | None=None
    supplier_id: int | None=None
    barcode: str | None=None
    
class   ProductRead(ProductBase):
    model_config=ConfigDict(from_attributes=True)
    
    product_id:str
    created_at:datetime