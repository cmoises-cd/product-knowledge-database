from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from controllers import product_addon_controller
from database import get_db
from schemas import productAddonSchema

router = APIRouter(prefix="/addons", tags=["Product Addons"])

# Create a new addon for a specific product
@router.post("/products/{product_id}/", response_model=productAddonSchema.ProductAddon)
def create_addon_for_product(product_id: int, addon: productAddonSchema.ProductAddonBase, db: Session = Depends(get_db)):
    return product_addon_controller.create_product_addon(db, addon, product_id)

# Get all addons for a specific product
@router.get("/products/{product_id}", response_model=list[productAddonSchema.ProductAddon])
def get_addons_by_product(product_id: int, db: Session = Depends(get_db)):
    addons = product_addon_controller.get_addons_by_product_id(db, product_id)
    if not addons:
        raise HTTPException(status_code=404, detail="Addons not found for this product")
    return addons

# Get a single addon by its ID
@router.get("/{addon_id}", response_model=productAddonSchema.ProductAddon)
def get_addon(addon_id: int, db: Session = Depends(get_db)):
    addon = product_addon_controller.get_addon_by_id(db, addon_id)
    if not addon:
        raise HTTPException(status_code=404, detail="Addon not found")
    return addon

# Update a specific addon by its ID
@router.put("/{addon_id}", response_model=productAddonSchema.ProductAddon)
def update_addon(addon_id: int, addon: productAddonSchema.ProductAddonBase, db: Session = Depends(get_db)):
    updated_addon = product_addon_controller.update_addon(db, addon_id, addon)
    if not updated_addon:
        raise HTTPException(status_code=404, detail="Addon not found")
    return updated_addon

# Delete an addon by its ID
@router.delete("/{addon_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_addon(addon_id: int, db: Session = Depends(get_db)):
    deleted_addon = product_addon_controller.delete_addon(db, addon_id)
    if not deleted_addon:
        raise HTTPException(status_code=404, detail="Addon not found")
    return {"message": "Addon successfully deleted"}