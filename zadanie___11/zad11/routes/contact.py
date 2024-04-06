from typing import List
from datetime import datetime, timedelta
from fastapi import APIRouter, HTTPException, Depends, status
from sqlalchemy.orm import Session
from zad11.database.db import get_db
from zad11.schemas import ContactModel,ContactResponse,ContactUpadate,ContactStatusUpadate
from zad11.repository import contact as repository_contact


router=APIRouter(prefix='/contact', tags='[contact]' )


@router.get('/', response_model=List[ContactResponse])
async def read_contact(skip: int=0, limit: int=30, db: Session= Depends(get_db)):
    contact= await repository_contact.get_contact(skip,limit,db)
    return contact

@router.get('/{id}',response_model=ContactResponse)
async def read_contac(id:int, db: Session= Depends(get_db)):
    contac= await repository_contact.get_contac(id, int, db)
    if contac is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Contact not found')
    return contac

@router.get('/{first_name}', response_model=ContactResponse)
async def read_contac( first_name:str, db: Session= Depends(get_db)):
    contac= await repository_contact.get_contact(first_name, str, db)
    if contac is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Contact not found')
    return contac

@router.get('/upcoming_birthdays', response_model=List[ContactResponse])
async def upcoming_birthdays(db: Session=Depends(get_db)):
    current_data=datetime.now().date()
    end_data=current_data+timedelta(days=7)
    contac= await repository_contact.get_contact_by_birthday_range(current_data, end_data, db)
    if contac is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Contact not found')
    return contac

@router.post('/',response_model=ContactResponse)
async def create_contact(body: ContactModel, db: Session= Depends(get_db)):
    return await repository_contact.get_contact(body,db)

@router.put('/{id}', response_model=ContactResponse)
async def upadate_contact(body: ContactUpadate, db:Session= Depends(get_db)):
    contac= await repository_contact.upadate_contac(id, int, db)
    if contac is  None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Contact not found')
    return contac

@router.patch('/{id}', response_model=ContactResponse)
async def upadate_status_contact(body: ContactStatusUpadate, db: Session=Depends(get_db)):
    contac= await repository_contact.upadate_status_contact(id, int, db)
    if contac is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Contact not found')
        return contac

@router.delete('/{id}', response_model=ContactResponse)
async def remove_contact(id: int,db: Session= Depends(get_db)):
    contac= await repository_contact.remove_contact(id, db)
    if contac is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Contact not found')
        return contac



