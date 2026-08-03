from repositories.product_repository import product_repository
from fastapi import HTTPException
from sqlalchemy.orm import Session 
from models.product import Product
from schemas.product import ProductCreate, ProductUpdate


def get_product(db: Session, id:int):
    product= product_repository.get(db, id)
    if not product:
        raise HTTPException(
            status_code= status.HTTP_404_NOT_FOUND, detail="Product not found")
    
    return product

def list_products(db:Session):
    return product_repository.get_all(db)

def create_product(db:Session, data:ProductCreate):
   # - save images on file
    #-update inventory stock
    #-send notfi
    return product_repository.create(db, data.model_dump())

def update_product(db:Session, product_id: int, data:ProductUpdate):
    product=product_repository(db, product_id)
    return product_repository.update(db, product, data.model_dump(exclude_unset=True))

def delete_product(db:Sesiion, product_id:int):
    # check permissions
    # check policies
    product=product_repository(db, product_id)
    product_repository.delete(db, product)
    
                                     
