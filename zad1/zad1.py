from collections import UserDict
from datetime import datetime
import re
import abc




class Field:
    def __init__(self, value):
        self.value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        self._value = new_value




class Name(Field):
    pass




class Phone(abc.ABC):
    @abc.abstractmethod
    def __init__(self, value):
        super().__init__(value)
        self.validate_phone()
    @abc.abstractmethod
    def validate_phone(self):
        # Sprawdzanie poprawności formatu numeru telefonu
        allowed_chars = set("0123456789+-()/. ")
        if not all(char in allowed_chars for char in self.value):
            raise ValueError("Invalid phone number format")

        digits = [char for char in self.value if char.isdigit()]
        if len(digits) != 9:
            raise ValueError("Phone number must have exactly 9 digits")




class Email(abc.ABC):
    @abc.abstractmethod
    def __init__(self, value):
        super().__init__(value)
        self.validate_email()
    @abc.abstractmethod
    def validate_email(self):
        # Sprawdzanie poprawności formatu adresu e-mail
        email_pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        if not re.match(email_pattern, self.value):
            raise ValueError("Invalid e-mail format")




class Birthday(abc.ABC):
    @abc.abstractmethod
    def __init__(self, value):
        super().__init__(value)
        self.validate_birthday()
    @abc.abstractmethod
    def validate_birthday(self):

        try:
            datetime.strptime(str(self.value), '%Y-%m-%d')
        except ValueError:
            raise ValueError("Invalid birthday format")



