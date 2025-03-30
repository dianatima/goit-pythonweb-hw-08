from datetime import datetime, date
from typing import Optional

from pydantic import BaseModel, Field, ConfigDict, EmailStr

from src.conf import constants
from src.conf import messages


class ContactSchema(BaseModel):
    first_name: str = Field(
        min_length=constants.COL_MIN_LENGTH,
        max_length=constants.COL_MAX_LENGTH,
        description=messages.contact_schema_name.get("ua"),
    )
    last_name: str = Field(
        min_length=constants.COL_MIN_LENGTH,
        max_length=constants.COL_MAX_LENGTH
    )
    email: EmailStr
    phone: str = Field(min_length=5, max_length=50)
    birthday: date
    info: Optional[str] = Field(default=None, max_length=255)


class ContactUpdateSchema(BaseModel):
    first_name: str = Field(default=None, min_length=3, max_length=100)
    last_name: str = Field(default=None, min_length=3, max_length=100)
    email: Optional[EmailStr] = None
    phone: str = Field(default=None, min_length=5, max_length=50)
    birthday: Optional[date] = None
    info: Optional[str] = Field(default=None, max_length=255)


class ContactResponse(BaseModel):
    id: int
    first_name: str
    last_name: str
    email: str
    phone: str
    birthday: date
    info: str = Field(default=None)
    model_config = ConfigDict(from_attributes=True)