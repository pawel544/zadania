from typing import List, Optional
from pydantic import BaseModel, Field


class ContactModel(BaseModel):
    first_name: str= Field(max_length=20)
    last_name: str= Field(max_length=30)
    number: int
    date_of_birth: int
    additional_information : str= Field(max_length=100)

class ContactResponse(ContactModel):
    id: int

    class Config:
        orm_mode= True
class ContactUpadate(ContactModel):
    done: bool

class ContactStatusUpadate(BaseModel):
    done: bool





