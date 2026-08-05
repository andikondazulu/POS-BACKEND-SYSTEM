from datetime import datetime
from pydantic import BaseModel, ConfigDict
from app.models.receipt import ReceiptType

class ReceiptBase(BaseModel):
    sale_id: str
    receipt_number: str
    receipt_type: ReceiptType
    receipt_data: str
    

class ReceiptCreate(ReceiptBase):
    pass

class ReceiptUpdate(BaseModel):
    receipt_number: str | None = None
    receipt_type: ReceiptType | None = None
    receipt_data: str | None = None
    

class ReceiptRead(ReceiptBase):
    model_config = ConfigDict(from_attributes=True)

    receipt_id: str
    generated_at: datetime