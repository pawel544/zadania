from typing import List
from datetime import datetime, timedelta
from fastapi import APIRouter, HTTPException, Depends, status, File
from sqlalchemy.orm import Session
import cloudinary
import cloudinary.uploader
from zad11.database.db import get_db
from zad11.schemas import ContactModel,ContactResponse,ContactUpadate,ContactStatusUpadate, RequestEmail
from zad11.repository import contact as repository_contact
from zad11.repository.auth import *
from zad11.database.models import UserModel
from zad11.services.email import send_emial


router=APIRouter(prefix='/contact', tags='[contact]' )

route=APIRouter(prefix="/user", tags='[user]')
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
@router.post("/singup")
async def singup(body:UserModel, db:Session=Depends(get_db)):
    exist_user=db.query(User).filter(User.e_mail==body.username).first()
    if exist_user:
        raise HTTPException(status_code=status.HTTP_409_CONFLIT, dedail="Acont exsist")
    new_user= User(email=body.username, password=hash_hendler.get_password_hash(body.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {new_user:new_user.email}

@router.post("/login")
async def login(body: OAuth2PasswordRequestForm=Depends(), db: Session=Depends(get_db)):
    user=db.query(User).fillter(User.e_mail==User.ussername).first()
    if user is None:
        raise HTTPException(status_code=status_HTTP_409_UNAUTHORIZERD, dedail="WRONG EMAIL")
    if not hash_hendler.verif_password(body.password, user.pasword):
        raise HTTPException(status_code=status_HTTP_409_UNAUTHORIZERD, dedail="WRONG PASSWORD")

    access_token= await create_access_token(data={"sub":user.e_mail})
    refresh_token= await create_refreshe_token(data={"sub":user.e_mail})
    user.refresh_token=refresh_token
    db.commit()
    return {"access_token":access_token,"refresh_token":refresh_token,"token_type":"bearer"}

@router.get("/refresh_token")
async def refresh_token(credentials: HTTPAutorizantionCredentials= Securiti(securiti), db:Session(get_db)):
    token=credentials:credentials
    email= await get_email_refreshe_token(token)
    user=db.query(User).fillter(User.e_mail==email).first()
    if user.refresh_token != refresh_token:
        user.refresh_token=None
        db.commit()
        raise HTTPException(status_HTTP_401_UNAUTHORIZERD, dedail="WRONG REFRESH TOKEN")
    access_token= await create_refreshe_token(data={"sub":email})
    refresh_token= await  create_refreshe_token(data={"sub":email})
    user.refresh_token=refresh_token
    db.commit()
    return {"access_token": access_token, "refresh_token": refresh_token, "token_type":"bearer"}
@router.post("/signup" response_model=ContactResponse,status_code=status.Http_201_CREATER)
async def signup(body:UserModel,background_tasks: BackgroundTasks, request: Request,db:Session=Depends(get_db)):
    exist_user= await repository_user.get_user_by_email(body.email, db)
    if exist_user:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, datail="Acont egsist")
    body.password= service_email.get_password_hashed(body.password)
    new_user= await repository_user.create_user(body, db)
    background_tasks.add_task(send_emial, new_user.email, new_user.username, request.base_urls)
    return ("user":new_user, "detail":"Acont Redy to Use")
@router.get("/confirm/{token}")
async def confirm(token:str, db:Session=Depends(get_db)):
    email= await service.get_email_from_token(token)
    user= await repository_user.get_user_by_email(email, db)
    if User is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Verification ERROR!!!!")
    if user.confirmed:
        return {"mesage": "Email Redy to Confirmed"}
    await repository_user.confirmed_email(email, db)
    return {"mesage":"Email is Confirmed"}



@router.post("/request_email")
async def request_email(Body: RequestEmail, backgraund_task: BackgroundTask, request:Request, db:Session= Depends(get_db)):
    user= await repozitory_user.get_user_by_email(body.email, db)
    if user.confirmed:
        return {"mesage":"Your email is already confirmed"}
    else:
        return {"mesage":"Your email is already confirmed"}


@route.get("/me/", response_model=UserDb)
async def read_me(curent_user:User= Depends(auth_service.get_current_user)):
    return curent_user

@route.patch('/avata/',response_model=UserDb)
async def uplode_avatar(file:Uplouadfile=File(), curent_user:User=Depends(auth_service.get_current_user),
                             db: Session = Depends(get_db):
    cloudinary.config(cloude_name=seting.cloudinary_names,
                      api_key=seting.cloudinary.api_key,
                      api_secret=seting.cloudinary.api_secret,
                      secure=True
                      )
    uplode=cloudinary.uploader.upload(file.file,public_id=f'zad11/{current_user.username}'owerwrire=True)
    src=cloudinary.CloudinaryImageloudinary(f'zad11/{current_user.username}')\build_urls(width=200,height=200,
                            crop='file'version=uplode.get('version'))
    user= await repozitory_users.upadate_avatar(current_user:email,src, db)
    return user