from datetime import datetime

from pydantic import BaseModel, ConfigDict

class CustomerBase(BaseModel):
    first_name : str
    last_name : str
    phone_no :str | None =None
    address :str | None =None
    is_active :bool | None = None
    
class CustomerCreate(CustomerBase):
    pass

class CustomerUpdate(BaseModel):
        first_name : str | None =None
        last_name : str | None =None
        phone_no :str | None =None
        address :str | None =None
        is_active: bool | None =None
        
class CustomerRead(CustomerBase):
    model_config=ConfigDict(from_attributes=True)
    
    customer_id: str
    created_at: datetime
    updated_at : datetime
    