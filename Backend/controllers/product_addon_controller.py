from sqlalchemy.orm import Session
from models.productsModel import ProductAddon as ProductAddonModel
from schemas.productAddonSchema import ProductAddonBase, ProductAddon as ProductAddonSchema, ProductAddonUpdate
from typing import Optional, List

# Add a new addon to a product
def create_product_addon(db: Session, addon: ProductAddonBase, product_id: int) -> ProductAddonModel:
    addon_data = addon.model_dump()
    addon_data['product_id'] = product_id
    db_addon = ProductAddonModel(**addon_data)
    db.add(db_addon)
    db.commit()
    db.refresh(db_addon)
    return db_addon

# Get addons by product ID
def get_addons_by_product_id(db: Session, product_id: int) -> List[ProductAddonModel]:
    return db.query(ProductAddonModel).filter(ProductAddonModel.product_id == product_id).all()

# Get a single addon by its primary key
def get_addon_by_id(db: Session, addon_id: int) -> Optional[ProductAddonModel]:
    return db.query(ProductAddonModel).filter(ProductAddonModel.id == addon_id).first()

# Update a specific addon by its ID
def update_addon(db: Session, addon_id: int, addon: ProductAddonUpdate) -> Optional[ProductAddonModel]:
    db_addon = db.query(ProductAddonModel).filter(ProductAddonModel.id == addon_id).first()
    if db_addon:
        for key, value in addon.model_dump(exclude_unset=True).items():
            setattr(db_addon, key, value)
        db.commit()
        db.refresh(db_addon)
        return db_addon
    return None

# Delete an addon by its ID
def delete_addon(db: Session, addon_id: int) -> Optional[ProductAddonModel]:
    db_addon = db.query(ProductAddonModel).filter(ProductAddonModel.id == addon_id).first()
    if db_addon:
        db.delete(db_addon)
        db.commit()
        return db_addon
    return None