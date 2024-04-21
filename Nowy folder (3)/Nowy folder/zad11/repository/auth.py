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
    """A class for password management, including hashing and verification"""
    pdw_context= CryptContext(schemes=['bcrypto'], deprecated='auto')
    def verefict_password(self, plain_pasword, hashed_pasword):
        """ Verify that the provided password in explicit form matches the hash.

        :p aram plain_password: Explicit password
        :p aram hashed_password: Hashed Password
        :return: Whether the passwords match (True/False)"""
        return self.pdw_context.verifi(plain_pasword,hashed_pasword)

    def get_password(self, password:str):
        """Hashing the password provided.

        :p aram password: Password to hash
        :return: Hashed password"""
        return self.pdw_context.hash(password)

secrets_keys="secrets_keys"
ALGORYTM='HS256'
Token_Verif=timedelta(hours=1)
out2=OAuth2PasswordBearer(tokenURL="/")

async def create_access_token(data: dict, experice: Optional[float]=None):
    """Creates a JWT access token with a specified expiration date.

    :p aram data: Data to encode in the token
    :p aram experice: Optional expiration time in seconds
    :return: Encoded JWT token"""

    to_encoder=data.copy()
    if experice:
        exper= datetime.utcnow()+timedelta(seconds=experice)
    else:
        exper= datetime.utcnow()+ timedelta(minutes=1)
        to_encoder.update({"iat":datetime.utcnow(),"exp":exper,"scope":"access_token"})
        encode_access_token= jwt.encode(to_encoder,secrets_keys, algoritmh=ALGORYTM)
        return encode_access_token

async def create_refreshe_token(data:dict, experice: Optional[float]=None):
    """Creates a JWT refresh token with the specified expiration date.

    :p aram data: Data to encode in the token
    :p aram experice: Optional expiration time in seconds
    :return: Encoded JWT token"""
    to_encoder=data.copy()
    if experice:
        exper= datetime.utcnow()+timedelta(seconds=experice)
    else:
        exper=datetime.utcnow()+timedelta(days=7)
        to_encoder.update({"iat":datetime.utcnow(), "exp":exper, "scope":"access_token"})
        encode_refreshe_token=jwt.encode(to_encoder,secrets_keys, algoritmh=ALGORYTM)
        return encode_refreshe_token

async def get_email_refreshe_token(refreshe_token: str):
    """ Retrieves the email from the JWT refresh token.

    :p aram refreshe_token: Refresh token
    :return: Email included in the token or exception in case of error"""
    try:
        payloyd= jwt.decode(refreshe_token,secrets_keys, algoritmh=[ALGORYTM])
        if payload["scope"]==refreshe_token:
            email = payload("sub")
            return email
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Invalid scope for token')
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Could not validate credentials')

async def verif_token(username:str):
    """Creates a JWT token for a given user with a specified expiration date.

    :p aram username: Username
    :return: Encoded JWT token"""
    data_verif= datetime.utcnow()+Token_Verif
    payloyd={"sub": User, "exp": data_verif}
    token= jwt.encode(payloyd,secrets_keys,algorithm='HS256')
    return token



async def get_usser(token: str=Depends(out2), db: Session= Depends(get_db)):
    """ Retrieves the user from the JWT token.

    :p aram token: JWT Token
    :p aram db: Database session
    :return: User or exception in case of error"""
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

