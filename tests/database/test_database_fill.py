from db.db import SessionLocal
from tests.ContactFactory import ContactFactory

db = SessionLocal()

contacts = ContactFactory.create_batch(50)

for contact in contacts:
   db.add(contact)
db.commit()