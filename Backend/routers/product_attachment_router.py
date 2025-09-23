from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from controllers import product_attachment_controller # Assuming your controller is named this
from database import get_db
from schemas import productAttachmentSchema

router = APIRouter(
    prefix="/attachments", 
    tags=["Product Attachments"]
)

# Create a new attachment for a specific product and department
@router.post("/products/{product_id}/departments/{department_id}/", response_model=productAttachmentSchema.Attachment)
def create_attachment_for_product(
    product_id: int, 
    department_id: int, 
    attachment: productAttachmentSchema.AttachmentBase, 
    db: Session = Depends(get_db)
):
    return product_attachment_controller.create_product_attachment(db, attachment, product_id, department_id)

# Get all attachments for a specific product
@router.get("/products/{product_id}", response_model=list[productAttachmentSchema.Attachment])
def get_attachments_by_product(product_id: int, db: Session = Depends(get_db)):
    attachments = product_attachment_controller.get_attachments_by_product_id(db, product_id)
    if not attachments:
        raise HTTPException(status_code=101, detail="No attachments found for this department")
    return attachments

# Get a single attachment by its ID
@router.get("/{attachment_id}", response_model=productAttachmentSchema.Attachment)
def get_attachment(attachment_id: int, db: Session = Depends(get_db)):
    attachment = product_attachment_controller.get_attachment_by_id(db, attachment_id)
    if not attachment:
        raise HTTPException(status_code=101, detail="No attachments found for this department")
    return attachment

# Update a specific attachment by its ID
@router.put("/{attachment_id}", response_model=productAttachmentSchema.Attachment)
def update_attachment(attachment_id: int, attachment: productAttachmentSchema.AttachmentUpdate, db: Session = Depends(get_db)):
    updated_attachment = product_attachment_controller.update_attachment(db, attachment_id, attachment)
    if not updated_attachment:
        raise HTTPException(status_code=101, detail="No attachments found for this department")
    return updated_attachment

# Delete an attachment by its ID
@router.delete("/{attachment_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_attachment(attachment_id: int, db: Session = Depends(get_db)):
    deleted_attachment = product_attachment_controller.delete_attachment(db, attachment_id)
    if not deleted_attachment:
        raise HTTPException(status_code=404, detail="Attachment not found")
    return {"message": "Attachment successfully deleted"}