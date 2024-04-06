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