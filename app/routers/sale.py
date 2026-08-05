from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from database import get_db
from app.schemas.sale import SalesUpdate, SalesCreate, SalesRead
from app.services import sale as sale_service

router = APIRouter(prefix="/sale", tags=["Sale"])


@router.get("/", response_model=list[SalesRead])
def list_sales(db: Session = Depends(get_db)):
    return sale_service.list_sales(db)


@router.get("/{sale_id}", response_model=SalesRead)
def get_sale(sale_id: str, db: Session = Depends(get_db)):
    return sale_service.get_sale(db, sale_id)


@router.post("/", response_model=SalesRead, status_code=status.HTTP_201_CREATED)
def create_sale(data: SalesCreate, db: Session = Depends(get_db)):
    return sale_service.create_sale(db, data)


@router.put("/{sale_id}", response_model=SalesRead)
def update_sale(
    sale_id: str, data: SalesUpdate, db: Session = Depends(get_db)
):
    return sale_service.update_sale(db, sale_id, data)


@router.delete("/{sale_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_sale(sale_id: str, db: Session = Depends(get_db)):
    return sale_service.delete_sale(db, sale_id)
