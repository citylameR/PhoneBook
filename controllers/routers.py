from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session


import db.models.contacts as models
from db.models.contacts_in import ContactIn
from db.db import get_db_session

router = APIRouter(
    prefix="/contacts"
)


def get_db():
    db = next(get_db_session())
    try:
        yield db
    finally:
        db.close()


@router.get('/')
async def get_contacts(db: Session = Depends(get_db)):
    contacts = db.query(models.Contact).all()
    return contacts


@router.get('/{contact_id}')
async def get_contact(contact_id: int, db: Session = Depends(get_db)):
    contact = db.query(models.Contact).get(contact_id)
    if not contact:
        raise HTTPException(status_code=404, detail="Contact not found")
    return contact


@router.post('/')
async def create_contact(contact: ContactIn, db: Session = Depends(get_db)):
    db_contact = models.Contact(**contact.dict())
    db.add(db_contact)
    db.commit()
    db.refresh(db_contact)
    return db_contact


@router.put('/{contact_id}')
async def update_contact(contact_id: int,
                         contact: ContactIn,
                         db: Session = Depends(get_db)):
    db_contact = db.query(models.Contact).get(contact_id)
    if not db_contact:
        raise HTTPException(status_code=404, detail="Contact not found")

    db_contact.first_name = contact.first_name
    db_contact.last_name = contact.last_name
    db_contact.company = contact.company
    db_contact.work_phone = contact.work_phone
    db_contact.personal_phone = contact.personal_phone

    db.add(db_contact)
    db.commit()
    db.refresh(db_contact)
    return db_contact


@router.delete('/{contact_id}')
async def delete_contact(contact_id: int, db: Session = Depends(get_db)):
    contact = db.query(models.Contact).get(contact_id)
    if not contact:
        raise HTTPException(status_code=404, detail="Contact not found")
    db.delete(contact)
    db.commit()
    return {"ok": True}
