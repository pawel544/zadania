from sqlalchemy import Column, Integer, String, Boolean, func, Table
from sqlalchemy.orm import Relationship
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import DateTime
from sqlalchemy.ext.declarative import declarative_base
Base=declarative_base()

class Contact(Base):
    """A class that represents a table of contacts in a database.

    :param id: A unique identifier for the contact.
    :param first_name: First name, maximum 20 characters, unique.
    :param last_name: Last name, maximum 30 characters, unique.
    :param number: The phone number, must be unique.
    :param date_of_birth: Year of birth.
    :param additional_information: Additional information, up to 100 characters, can be blank."""
    __tablename__="contact"
    id=Column(Integer, primary_key=True)
    first_name=Column(String(20), nullable=False, unique=True)
    last_name=Column(String(30),nullable=False, unique=True)
    number=Column(Integer, nullable=False, unique=True)
    date_of_birth=Column(Integer,nullable=False)
    additional_information=Column(String(100), nullable=True, unique=False)

class User (Base):
    """A class that represents a table of users in a database.

    :param id: A unique identifier for the user.
    :param e_mail: Email address, unique.
    :param pasword: The user's password.
    :param refresh_token: Session refresh token, optional."""
    __tablename__="user"
    id=Column(Integer,primary_key=True)
    e_mail=Column(String(100),nullable=False,unique=True)
    pasword=Column(String(100),nullable=False)
    refresh_token=Column(String(300), nullable=True)
class UserModel(Base):
    """User input model.

    :param username: The username.
    :param password: The user's password."""
    username:str
    password: str
