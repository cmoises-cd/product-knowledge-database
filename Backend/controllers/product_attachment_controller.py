from sqlalchemy.orm import Session
from models.productsModel import Attachment as ProductAttachmentModel
from schemas.productAttachmentSchema import AttachmentBase, AttachmentUpdate
from typing import Optional, List

# Add a new attachment to a product
def create_product_attachment(db: Session, attachment: AttachmentBase, product_id: int, department_id: int) -> ProductAttachmentModel:
    attachment_data = attachment.model_dump()
    attachment_data['product_id'] = product_id
    attachment_data['department_id'] = department_id
    db_attachment = ProductAttachmentModel(**attachment_data)
    db.add(db_attachment)
    db.commit()
    db.refresh(db_attachment)
    return db_attachment

# Get all attachments for a specific product
def get_attachments_by_product_id(db: Session, product_id: int) -> List[ProductAttachmentModel]:
    return db.query(ProductAttachmentModel).filter(ProductAttachmentModel.product_id == product_id).all()

# Get a single attachment by its primary key
def get_attachment_by_id(db: Session, attachment_id: int) -> Optional[ProductAttachmentModel]:
    return db.query(ProductAttachmentModel).filter(ProductAttachmentModel.id == attachment_id).first()

# Update a specific attachment by its ID
def update_attachment(
    db: Session, 
    attachment_id: int, 
    attachment: AttachmentUpdate
) -> Optional[ProductAttachmentModel]:
    db_attachment = db.query(ProductAttachmentModel).filter(ProductAttachmentModel.id == attachment_id).first()
    if db_attachment:
        for key, value in attachment.model_dump(exclude_unset=True).items():
            setattr(db_attachment, key, value)
        db.commit()
        db.refresh(db_attachment)
        return db_attachment
    return None

# Delete an attachment by its ID
def delete_attachment(db: Session, attachment_id: int) -> Optional[ProductAttachmentModel]:
    db_attachment = db.query(ProductAttachmentModel).filter(ProductAttachmentModel.id == attachment_id).first()
    if db_attachment:
        db.delete(db_attachment)
        db.commit()
        return db_attachment
    return None