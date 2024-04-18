from sqlalchemy import Column, Integer, String, Boolean, func, Table
from sqlalchemy.orm import Relationship
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import DateTime
from sqlalchemy.ext.declarative import declarative_base
Base=declarative_base()

class Contact(Base):
    __tablename__="contact"
    id=Column(Integer, primary_key=True)
    first_name=Column(String(20), nullable=False, unique=True)
    last_name=Column(String(30),nullable=False, unique=True)
    number=Column(Integer, nullable=False, unique=True)
    date_of_birth=Column(Integer,nullable=False)
    additional_information=Column(String(100), nullable=True, unique=False)

class User (Base):
    __tablename__="user"
    id=Column(Integer,primary_key=True)
    e_mail=Column(String(100),nullable=False,unique=True)
    pasword=Column(String(100),nullable=False)
    refresh_token=Column(String(300), nullable=True)
class UserModel(Base):
    username:str
    password: str
