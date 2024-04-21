from typing import List
from sqlalchemy.orm import Session
from zad11.schemas import ContactResponse, ContactUpadate ,ContactStatusUpadate, ContactModel
from zad11.database.models import Contact
from datetime import datetime,timedelta


async def get_contact(skip: int, limit: int, db: Session)-> List[Contact]:
    """Returns a list of contacts with the specified offset and limit.

    :p param skip: Number of contacts to skip (offset)
    :p param limit: The maximum number of contacts to return
    :p param db: Database session
    :return: Contact list"""
    return db.query(Contact).offset(skip).limit(limit).all()

async  def get_contact(id:int,db:Session)->Contact:
    """  Returns a contact based on the given ID.

    :p param id: Contact ID
    :p param db: Database session
    :return: Contact, or None if not found"""
    return db.query(Contact).filter(Contact.id==id).first()

async def get_contact(first_names:str, db:Session )-> Contact:
    """ Returns a list of contacts based on the given name.

    :p param first_names: Contact name
    :p param db: Database session
    :return: A list of contacts with the given name"""
    return  db.query(Contact).filter(Contact.first_name==first_names).all()

async def upcoming_birthdays(current_data:datetime,db:Session)->List[Contact]:
    """ Returns a list of contacts who have birthdays in the next 7 days.

    :p param current_data: Current Date
    :p param db: Database session
    :return: A list of contacts with an upcoming birthday"""

    end_data=current_data+timedelta(days=7)
    return db.query(Contact).filter(Contact.date_of_birth.between(current_data,end_data)).all


async def create_contact(body: ContactModel, db: Session)-> Contact:
    """Creates a new contact based on the data from the model.

    :p param body: Contact Details
    :p param db: Database session
    :return: Created contact"""
    contac= contact = Contact(first_name=body.first_name, last_name=body.last_name, number=body.number,
                              date_of_birth=body.date_of_birth, additional_information=body.additional_information)
    db.add(contac)
    db.commit()
    db.refresh(contac)
    return contac
async def remove_contact(id: int, db: Session)-> Contact|None:
    """ Deletes a contact based on the ID.

    :param id: Contact ID
    :param db: Database session
    :return: Deleted contact, or None if not found"""
    contac=db.query(Contact).filter(Contact.id==id).first()
    if contac:
        db.delete(contac)
        db.commit()
    return contac

async def upadate_contact(id: int, body: ContactModel, db: Session)-> Contact| None:
    """Updates an existing contact based on the specified ID.

    :pparam id: Contact ID
    :pparam body: Contact details to update
    :pparam db: Database session
    :return: Updated contact, or None if not found"""
    contac=db.query(Contact).filter(Contact.id==id).first()
    if contac:
        contac.title=body.tltle
        contac.description= body.description
        contac.done= body.done
        db.commit()
    return contac

async def upadate_status_contact(id: int, body: ContactStatusUpadate, db: Session)-> Contact| None:
    """Updates the status of the contact based on the provided ID.

    :pparam id: Contact ID
    :pparam body: New contact status
    :pparam db: Database session
    :return: Updated contact, or None if not found"""
    contac=db.query(Contact).filter(Contact.id==id).first()
    if contac:
        contac.done=contac.done
        db.commit()
    return contac

