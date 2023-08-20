import os
from pathlib import Path

from fastapi import Depends, Query, HTTPException, APIRouter
from sqlalchemy.orm import Session

from controllers.routers import get_db
import db.models.contacts as models
from utils.conversion_data import contacts_to_json

router = APIRouter(prefix="/export")


@router.get("/")
async def export_contacts(
        db: Session = Depends(get_db)
):
    contacts = db.query(models.Contact).all()

    data = contacts_to_json(contacts)
    filename = "contacts.json"

    project_root = Path(__file__).parent.parent
    output_path = os.path.join(project_root, filename)

    with open(output_path, "w+", encoding='utf-8') as f:
        f.write(data)

    return {"exported_to": output_path}
