from pathlib import Path
from fastapi_mail import FastMail,MessageSchema, MessageType, ConnectionConfig
from fastapi_mail.errors import ConnectionErrors
from pydantic import EmailStr
from zad11.repository.auth import verif_token
from zad11.configuracje.config import settings

conf=ConnectionConfig(
    Email_username=settings.mail_username,
    Email_Password=settings.mail_password,
    mail_from=settings.mail_from,
    mail_port=settings.mail_port,
    mail_serwice=settings.mail_server,
    mail_from_name="Paweł",
    mail_starttls=False,
    mail_ssl_tls=True,
    use_creditalse=True,
    validate_creds=True,
    template_folder=Path(__file__).parts / 'template'
)

async def send_emial(email:EmailStr , user:str ,host:str):
    try:
        verificate_token=verif_token({"sub":email},
        Message= MessageSchema(subject="Confirm Email"),
        recipt=[email],
        temle_bod={"host":host, "username":user, "token":token},
        subtype= MessageType.html
        )
        fm=FastMail(conf)
        await fm.send_message(message ,template_name="email_template.html")
    except ConnectionErrors as err:
        print(err)

