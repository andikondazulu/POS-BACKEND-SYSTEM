from datetime import datetime
from app.models.user import UserRole

from pydantic import BaseModel, ConfigDict

class UserBase(BaseModel):
    password : str
    first_name : str
    last_name : str
    email: str
    role: UserRole
    is_active :bool | None = None
    
class UserCreate(UserBase):
    pass

class UserUpdate(BaseModel):
        password : str | None =None
        name : str | None =None
        last_name : str | None =None
        email: str | None =None
        role: UserRole | None =None
        is_active: bool | None =None
        
class UserRead(UserBase):
    model_config=ConfigDict(from_attributes=True)
    
    User_id: str
    created_at: datetime
    updated_at : datetime
    