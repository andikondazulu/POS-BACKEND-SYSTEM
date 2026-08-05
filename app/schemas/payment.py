from datetime import datetime
from decimal import Decimal
from app.models.payment import PaymentMethod, PaymentStatus
from pydantic import BaseModel, ConfigDict


class PaymentBase(BaseModel):
    sale_id: str
    payment_method : PaymentMethod
    amount: Decimal
    payment_date: datetime
    status: PaymentStatus
    

class PaymentCreate(PaymentBase):
    pass

class PaymentUpdate(BaseModel):
    payment_method : PaymentMethod | None = None
    amount: Decimal | None = None
    payment_date: datetime | None = None
    status: PaymentStatus | None = None
    

class PaymentRead(PaymentBase):
    model_config = ConfigDict(from_attributes=True)

    payment_id: str