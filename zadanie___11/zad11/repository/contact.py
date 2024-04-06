from typing import List
from sqlalchemy.orm import Session
from zad11.schemas import ContactResponse, ContactUpadate ,ContactStatusUpadate, ContactModel
from zad11.database.models import Contact
from datetime import datetime,timedelta


async def get_contact(skip: int, limit: int, db: Session)-> List[Contact]:
    return db.query(Contact).offset(skip).limit(limit).all()

async  def get_contact(id:int,db:Session)->Contact:
    return db.query(Contact).filter(Contact.id==id).first()

async def get_contact(first_names:str, db:Session )-> Contact:
    return  db.query(Contact).filter(Contact.first_name==first_names).all()

async def upcoming_birthdays(current_data:datetime,db:Session)->List[Contact]:
    end_data=current_data+timedelta(days=7)
    return db.query(Contact).filter(Contact.date_of_birth.between(current_data,end_data)).all


async def create_contact(body: ContactModel, db: Session)-> Contact:
    contac= contact = Contact(first_name=body.first_name, last_name=body.last_name, number=body.number,
                              date_of_birth=body.date_of_birth, additional_information=body.additional_information)
    db.add(contac)
    db.commit()
    db.refresh(contac)
    return contac
async def remove_contact(id: int, db: Session)-> Contact|None:
    contac=db.query(Contact).filter(Contact.id==id).first()
    if contac:
        db.delete(contac)
        db.commit()
    return contac

async def upadate_contact(id: int, body: ContactModel, db: Session)-> Contact| None:
    contac=db.query(Contact).filter(Contact.id==id).first()
    if contac:
        contac.title=body.tltle
        contac.description= body.description
        contac.done= body.done
        db.commit()
    return contac

async def upadate_status_contact(id: int, body: ContactStatusUpadate, db: Session)-> Contact| None:
    contac=db.query(Contact).filter(Contact.id==id).first()
    if contac:
        contac.done=contac.done
        db.commit()
    return contac

