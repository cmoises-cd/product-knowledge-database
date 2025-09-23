from fastapi import FastAPI
from database import SessionLocal, engine, Base
from models import productsModel
from routers import product_router,product_attachment_router ,product_addon_router, product_department_router

# Connect to the database
def connect_to_db():
    try:
        # Create the database tables
        Base.metadata.create_all(bind=engine)
        print("Connected to the database successfully!")
    except Exception as e:
        print(f"Error connecting to the database: {e}")

# Create a FastAPI "instance"
app = FastAPI(on_startup=[connect_to_db])

# Include the product routers
app.include_router(product_router.router)
app.include_router(product_addon_router.router)
app.include_router(product_attachment_router.router)
app.include_router(product_department_router.router)

# Define a path operation decorator for the root path ("/")
@app.get("/")
def read_root():
    return {"Message": "Welcome to the Product information Management System API!",
            "Version": "1.0.0",
            "Description": "This API allows you to manage products, their addons, and attachments."}