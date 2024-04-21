from datetime import datetime,timedelta
from typing import Optional
from fastapi import Depends, HTTPException
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from jose import JWTError, jwt
from starlette import status
from zad11.database.db import get_db
from zad11.database.models import User




class Hash:
    pdw_context= CryptContext(schemes=['bcrypto'], deprecated='auto')
    def verefict_password(self, plain_pasword, hashed_pasword):
        return self.pdw_context.verifi(plain_pasword,hashed_pasword)

    def get_password(self, password:str):
        return self.pdw_context.hash(password)

secrets_keys="secrets_keys"
ALGORYTM='HS256'
Token_Verif=timedelta(hours=1)
out2=OAuth2PasswordBearer(tokenURL="/")

async def create_access_token(data: dict, experice: Optional[float]=None):
    to_encoder=data.copy()
    if experice:
        exper= datetime.utcnow()+timedelta(seconds=experice)
    else:
        exper= datetime.utcnow()+ timedelta(minutes=1)
        to_encoder.update({"iat":datetime.utcnow(),"exp":exper,"scope":"access_token"})
        encode_access_token= jwt.encode(to_encoder,secrets_keys, algoritmh=ALGORYTM)
        return encode_access_token

async def create_refreshe_token(data:dict, experice: Optional[float]=None):
    to_encoder=data.copy()
    if experice:
        exper= datetime.utcnow()+timedelta(seconds=experice)
    else:
        exper=datetime.utcnow()+timedelta(days=7)
        to_encoder.update({"iat":datetime.utcnow(), "exp":exper, "scope":"access_token"})
        encode_refreshe_token=jwt.encode(to_encoder,secrets_keys, algoritmh=ALGORYTM)
        return encode_refreshe_token

async def get_email_refreshe_token(refreshe_token: str):
    try:
        payloyd= jwt.decode(refreshe_token,secrets_keys, algoritmh=[ALGORYTM])
        if payload["scope"]==refreshe_token:
            email = payload("sub")
            return email
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Invalid scope for token')
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Could not validate credentials')

async def verif_token(username:str):
    data_verif= datetime.utcnow()+Token_Verif
    payloyd={"sub": User, "exp": data_verif}
    token= jwt.encode(payloyd,secrets_keys,algorithm='HS256')
    return token



async def get_usser(token: str=Depends(out2), db: Session= Depends(get_db)):
    cr_exception=HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Could not validate credentials",
                               headers={"WWW-Authenticate":"Bearer"})
    try:
        payloyd= jwt.decode(token, secrets_keys, algoritmh=[ALGORYTM])
        if payloyd["scope"]!= "access_token":
            raise  cr_exception
        email=payloyd["sub"]
        if email==None:
            raise  cr_exception
    except JWTError as e:
        raise  cr_exception
    user: User=db.query(User).filter(User.e_mail==email).first
    if user== None:
        raise  cr_exception
    return user

