import unittest
from unittest.mock import MagicMock
from sqlalchemy.orm import Session
from datetime import datetime
from venv.zad11.database.models import Contact, User, UserModel
from venv.zad11.schemas import ContactModel, ContactResponse
from venv.zad11.routes.contact import read_contac, upcoming_birthdays, create_contact


class TestNot(unittest.IsolatedAsyncioTestCase):
    def setUp(self):
        self.session=MagicMock(spec=Session)
        self.user=User(id=1)
    async def test_read_contact(self):
        contact=[Contact(),Contact(),Contact(),Contact()]
        self.session.query().filter().offset.limit().all.return_value=contact
        result= await read_contac(skip=0, limit=5, email=self.email, number=self.number, db=self.session)
        self.assertEqual(result,contact)
    async def test_upcoming_birthdays(self):
        contact=[Contact(),Contact(),Contact]
        self.session.query().filter().all.return_value=contact
        dat=datetime.now()
        result= await upcoming_birthdays(dat,db=self.session)
        self.assertEqual(result,contact)
    async def test_create_contact(self):
        body=Contact(first_name="Paweł",
    last_name="Wojtas",
    number="64646347373",
    date_of_birth="1999-01-10",
    additional_information="lalalala")
        rezult= await create_contact(body,db=self.session)
        self.assertEqual(rezult,body)
        self.assertEqual(rezult.first_name,body.first_name)
        self.assertEqual(rezult.last_name,body.last_name)
        self.assertEqual(rezult.date_of_birth,body.date_of_birth)
        self.assertEqual(rezult.additional_information,body.additional_information)



if __name__ == '__main__':
    unittest.main()
