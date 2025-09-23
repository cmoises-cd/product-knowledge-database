from sqlalchemy import Column, Integer, String, TIMESTAMP, TEXT, DATE, ForeignKey,Numeric
from sqlalchemy.dialects.postgresql import TEXT
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, relationship
from database import Base
class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255))
    brand = Column(String(255))
    status = Column(String(50))
    note = Column(TEXT)
    article = Column(String(100))
    asin = Column(String(50))
    ean = Column(String(50))
    description = Column(TEXT)
    parentage_identifier = Column(String(100))
    amazon_fba_sku = Column(String(100))
    amazon_mfn_sku = Column(String(100))
    shopify_sku = Column(String(100))
    otto_sku = Column(String(100))
    kaufland_sku = Column(String(100))
    created_at = Column(TIMESTAMP(timezone=True))
    updated_at = Column(TIMESTAMP(timezone=True))
    launch_date = Column(DATE)
    sku = Column(String)

    packaging = relationship("ProductPackaging", backref="product", cascade="all, delete-orphan")
    addons = relationship("ProductAddon", backref="product", cascade="all, delete-orphan")
    features = relationship("ProductFeature", backref="product", cascade="all, delete-orphan")
    inclusions = relationship("ProductInclusion", backref="product", cascade="all, delete-orphan")
    attachments = relationship("Attachment", backref="product", cascade="all, delete-orphan")



class ProductPackaging(Base):
    __tablename__ = "product_packaging"
    id = Column(Integer, primary_key=True, autoincrement=True)
    product_id = Column(Integer, ForeignKey("products.id"), nullable=False)
    packaging = Column(String(255))
    pallet_size = Column(String(100))
    packaging_dimensions = Column(String(100))
    packaging_weight = Column(Numeric(10, 2))
    target_fba_fee = Column(Numeric(10, 2))
    target_fbm_fee = Column(Numeric(10, 2))
    hermes_fbm_fee = Column(Numeric(10, 2))
    gls_fbm_fee = Column(Numeric(10, 2))
    created_at = Column(TIMESTAMP(timezone=True))
    updated_at = Column(TIMESTAMP(timezone=True))
class ProductAddon(Base):
    __tablename__ = 'product_addons'
    id = Column(Integer, primary_key=True, autoincrement=True)
    product_id = Column(Integer, ForeignKey("products.id"), nullable=False)
    addons_name = Column(String(255))
    addons_description = Column(TEXT)
class ProductFeature(Base):
    __tablename__ = 'product_features'
    id = Column(Integer, primary_key=True, autoincrement=True)
    product_id = Column(Integer, ForeignKey("products.id"), nullable=False)
    feature_name = Column(String(255))
    feature_description = Column(TEXT)
class ProductInclusion(Base):
    __tablename__ = 'product_inclusions'
    id = Column(Integer, primary_key=True, autoincrement=True)
    product_id = Column(Integer, ForeignKey("products.id"), nullable=False)
    inclusion_quantity = Column(Integer)
    inclusion_title = Column(TEXT)
class Department(Base):
    __tablename__ = 'departments'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), unique=True, nullable=False)
    
    # Relationship to the attachments table
    attachments = relationship("Attachment", backref="department", cascade="all, delete-orphan")
class Attachment(Base):
    __tablename__ = 'attachments'
    id = Column(Integer, primary_key=True, autoincrement=True)
    product_id = Column(Integer, ForeignKey("products.id"), nullable=False)
    # Corrected ForeignKey to point to 'departments.id'
    department_id = Column(Integer, ForeignKey("departments.id"))
    file_url = Column(TEXT)
    note = Column(TEXT)
    created_at = Column(TIMESTAMP(timezone=True))