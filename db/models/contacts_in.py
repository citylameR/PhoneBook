from typing import Optional

from pydantic import BaseModel


class ContactIn(BaseModel):
    first_name: str
    last_name: str
    middle_name: Optional[str] = None
    company: Optional[str] = None
    work_phone: Optional[str] = None
    personal_phone: Optional[str] = None

    class Config:
        from_attributes = True
        populate_by_name = True
