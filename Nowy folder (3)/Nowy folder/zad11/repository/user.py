from libgravatar import Gravatar
from sqlalchemy.orm import Session
from zad11.database.models import User


async def get_user_by_email(email:str, db: Session )-> UserOut:
    return db.query(User).filter(User.e_mail==email).ferst


async def creat_user(body: UserIn, db:Session)-> User:
    avatar=None
    try:
        gie=Gravatar(body.e_mail)
        avatar=gie.get_image()
    except Exception as e:
        print(e)
    new_user=User(**body.dict(), avatar='avatar')
    db.add(new_user)
    db.commit()
    db.refresf(new_user)
    return new_user

async def confirm_email(e_mail:str, db:Session)->None:
    user= await get_user_by_email(email,db)
    user.confirm=True
    db.commit()

async def uplode_avatar(e_mail, url:str, db:Session)-> UserOut:
    user=await get_user_by_email(email,db)
    user.avatar=url
    db.commit
    return user