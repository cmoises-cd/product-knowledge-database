from sqlalchemy.orm import Session
from models.productsModel import Product
from schemas import productSchema

# Create a new product
def create_product(db: Session, product: productSchema.ProductCreate):
    db_product = Product(**product.dict())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

# Get a product by ID
def get_product(db: Session, product_id: int):
    return db.query(Product).filter(Product.id == product_id).first()

# Get all products
def get_products(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Product).offset(skip).limit(limit).all()

# Update a product by ID
def update_product(db: Session, product_id: int, product: productSchema.ProductUpdate):
    db_product = db.query(Product).filter(Product.id == product_id).first()
    if db_product:
        ##update the object's attributes with new data from the Pydantic model
        for key, value in product.dict(exclude_unset=True).items():
            setattr(db_product, key, value)
        db.commit()
        db.refresh(db_product)
    return db_product

# Delete a product by ID
def delete_product(db: Session, product_id: int):
    db_product = db.query(Product).filter(Product.id == product_id).first()
    if db_product:
        db.delete(db_product)
        db.commit()
        
    return db_product