from fastapi_mail import ConnectionConfig, MessageSchema, MessageType, FastMail
from pydantic import EmailStr
import asyncio

from app.config import settings


class EmailServices:

    conf = ConnectionConfig(
        MAIL_USERNAME=settings.MAIL_USERNAME,
        MAIL_PASSWORD=settings.MAIL_PASSWORD,
        MAIL_PORT=settings.MAIL_PORT,
        MAIL_SERVER=settings.MAIL_SERVER,
        MAIL_FROM=settings.MAIL_FROM,
        MAIL_STARTTLS=False,
        MAIL_SSL_TLS=False,
    )

    @staticmethod
    def send_email(email: EmailStr):
        html = """<p>Hopefully, YOU logged into your account!</p> """

        message = MessageSchema(
            subject="Someone logged into your account please check your activity log.",
            recipients=[email],
            body=html,
            subtype=MessageType.html,
        )

        fm = FastMail(EmailServices.conf)
        asyncio.run(fm.send_message(message))
        return

    @staticmethod
    def send_email_win(email: EmailStr):
        html = """<p>Congratulations, you won!</p> """

        message = MessageSchema(
            subject="Your quiz results are in!!.",
            recipients=[email],
            body=html,
            subtype=MessageType.html,
        )

        fm = FastMail(EmailServices.conf)
        asyncio.run(fm.send_message(message))
        print("HEREEE")
        return

    @staticmethod
    def send_email_lose(email: EmailStr):
        html = """<p>Congratulations, you lost!</p> """

        message = MessageSchema(
            subject="Your quiz results are in!!.",
            recipients=[email],
            body=html,
            subtype=MessageType.html,
        )

        fm = FastMail(EmailServices.conf)
        asyncio.run(fm.send_message(message))
        print("HEREEE")
        return

    @staticmethod
    def send_email_draw(email: EmailStr):
        html = """<p>Good effort, it was a draw!</p> """

        message = MessageSchema(
            subject="Your quiz results are in!!.",
            recipients=[email],
            body=html,
            subtype=MessageType.html,
        )

        fm = FastMail(EmailServices.conf)
        asyncio.run(fm.send_message(message))
        return
