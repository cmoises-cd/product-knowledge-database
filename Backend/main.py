from fastapi import FastAPI
from database import SessionLocal, engine, Base
from models import productsModel
from routers import product_router
from routers import product_addon_router
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

# Include the product router
app.include_router(product_router.router)
app.include_router(product_addon_router.router)
# Define a path operation decorator for the root path ("/")
@app.get("/")
def read_root():
    return {"Hello": "World"}