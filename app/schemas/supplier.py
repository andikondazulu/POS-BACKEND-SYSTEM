from datetime import datetime

from pydantic import ConfigDict, BaseModel

class SupplierBase( BaseModel):
    company_name: str
    contact_name: str | None = None
    email:str | None = None
    supplier_phone: str | None = None
    address: str | None = None
    is_active: bool | None = None
    
class SupplierCreate(SupplierBase):
    pass

class SupplierUpdate( BaseModel):
    company_name: str | None = None
    contact_name: str | None = None
    email:str | None = None
    supplier_phone: str | None = None
    address: str | None = None
    is_active: bool | None = None
    
class SupplierRead(SupplierBase):
    model_config = ConfigDict(from_attributes=True)
    
    supplier_id: str