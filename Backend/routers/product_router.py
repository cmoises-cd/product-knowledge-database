from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from controllers import product_controller
from database import SessionLocal
from schemas import productSchema
from database import get_db
router = APIRouter(prefix="/products",tags=["Products"])

# Create a new product
@router.post("/", response_model=productSchema.ProductBase)
def create_product(product: productSchema.ProductCreate, db: Session = Depends(get_db)):
    return product_controller.create_product(db, product)

# Get all products
@router.get("/", response_model=list[productSchema.Product])
def get_products(db: Session = Depends(get_db)):
    response=product_controller.get_products(db)
    if response is None:
        raise HTTPException(status_code=404, detail="No products found")
    else :
        return response
# Get a product by ID
@router.get("/{product_id}", response_model=productSchema.Product)
def get_product(product_id: int, db: Session = Depends(get_db)):
    db_product = product_controller.get_product(db, product_id)
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return db_product

# Update a product by ID
@router.put("/{product_id}", response_model=productSchema.ProductUpdate)
def update_product(product_id: int, product: productSchema.ProductUpdate, db: Session = Depends(get_db)):
    return product_controller.update_product(db, product_id, product)

# Delete a product by ID
@router.delete("/{product_id}", response_model=productSchema.Product)
def delete_product(product_id:int, db:Session = Depends(get_db)):
    response=product_controller.delete_product(db, product_id)
    if response is None:
        raise HTTPException(status_code=404, detail="Product not found")