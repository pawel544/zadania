from typing import List, Optional
from pydantic import BaseModel, Field, EmailStr


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

class UserIn(BaseModel):
    username: str= Field(min_lenght=4, max_lenght=15)
    email:str
    password:str= Field(min_lenght=7, max_lenght=50)

class UserOut(BaseModel):
    id:str
    username:str
    email:str
    avatar: str
class UserResponse(BaseModel):
    username:str

class RequestEmail:
    email: EmailStr

