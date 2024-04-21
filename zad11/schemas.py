from typing import List, Optional
from pydantic import BaseModel, Field, EmailStr


class ContactModel(BaseModel):
    """A model to represent contact data.

    :param first_name: First name, maximum 20 characters.
    :param last_name: Last name, maximum 30 characters.
    :param number: The phone number as an integer.
    :param date_of_birth: Year of birth as a whole number.
    :param additional_information: Additional information, maximum 100 characters."""
    first_name: str= Field(max_length=20)
    last_name: str= Field(max_length=30)
    number: int
    date_of_birth: int
    additional_information : str= Field(max_length=100)

class ContactResponse(ContactModel):
    """Model to an API response containing information about the contact, along with an ID.

    :param id: A unique identifier for the contact."""
    id: int

    class Config:
        orm_mode= True
class ContactUpadate(ContactModel):
    """A model to update contact information.

    :param done: Flag indicating whether the contact's task has been completed."""
    done: bool

class ContactStatusUpadate(BaseModel):
    """A model to update the contact's status.

    :param done: Flag indicating whether the task has been completed."""
    done: bool

class UserIn(BaseModel):
    """The model for user input when creating an account.

    :param username: Username, 4 to 15 characters long.
    :param email: The user's email address.
    :param password: Password, between 7 and 50 characters long."""
    username: str= Field(min_lenght=4, max_lenght=15)
    email:str
    password:str= Field(min_lenght=7, max_lenght=50)

class UserOut(BaseModel):
    """The model for the user's output in the API response.

    :param id: A unique identifier for the user.
    :param username: The username.
    :param email: E-mail address.
    :param avatar: The URL to the user's avatar."""
    id:str
    username:str
    email:str
    avatar: str
class UserResponse(BaseModel):
    """Model to a response that includes the user's name.

    :param username: The username."""
    username:str

class RequestEmail:
    """ Model to request email for verification.

    :param email: The user's email address."""
    email: EmailStr

