from collections import UserDict
from datetime import datetime
import re

# Klasa reprezentująca pojedyncze pole w rekordzie


class Field:
    def __init__(self, value):
        self.value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        self._value = new_value

# Klasa dziedzicząca po Field, reprezentująca imię


class Name(Field):
    pass

# Klasa dziedzicząca po Field, reprezentująca numer telefonu


class Phone(Field):
    def __init__(self, value):
        super().__init__(value)
        self.validate_phone()

    def validate_phone(self):
        # Sprawdzanie poprawności formatu numeru telefonu
        allowed_chars = set("0123456789+-()/. ")
        if not all(char in allowed_chars for char in self.value):
            raise ValueError("Invalid phone number format")

        digits = [char for char in self.value if char.isdigit()]
        if len(digits) != 9:
            raise ValueError("Phone number must have exactly 9 digits")

# Klasa dziedzicząca po Field, reprezentująca adres e-mail


class Email(Field):
    def __init__(self, value):
        super().__init__(value)
        self.validate_email()

    def validate_email(self):
        # Sprawdzanie poprawności formatu adresu e-mail
        email_pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        if not re.match(email_pattern, self.value):
            raise ValueError("Invalid e-mail format")

# Klasa dziedzicząca po Field, reprezentująca datę urodzenia


class Birthday(Field):
    def __init__(self, value):
        super().__init__(value)
        self.validate_birthday()

    def validate_birthday(self):
        # Sprawdzanie poprawności formatu daty urodzenia
        try:
            datetime.strptime(str(self.value), '%Y-%m-%d')
        except ValueError:
            raise ValueError("Invalid birthday format")

# Klasa reprezentująca pojedynczy rekord w książce adresowej


class Record:
    # Słownik mapujący typy pól na odpowiadające im klasy
    FIELD_CLASSES = {
        "phones": Phone,
        "emails": Email,
        "birthday": Birthday,
    }

    def __init__(self, name, birthday=None):
        if not name:
            raise ValueError("Name is required.")
        self.name = Name(name)
        self.fields = {"phones": [], "emails": [], "birthday": []}
        if birthday:
            self.add_field("birthday", birthday)

    def add_field(self, field_type, value):
        # Dodawanie nowego pola do rekordu
        if field_type in self.fields and field_type in self.FIELD_CLASSES:
            field_class = self.FIELD_CLASSES[field_type]
            try:
                self.fields[field_type].append(field_class(value))
            except ValueError as e:
                print(f"Error adding field: {field_type}: {e}")

    def remove_field(self, field_type, value):
        # Usuwanie pola z rekordu
        if field_type in self.fields:
            self.fields[field_type] = [
                f for f in self.fields[field_type] if f.value != value]

    def edit_field(self, field_type, old_value, new_value):
        # Edytowanie istniejącego pola w rekordzie
        if field_type in self.fields:
            for field in self.fields[field_type]:
                if field.value == old_value:
                    field.value = new_value
                    break

    def days_to_birthday(self):
        # Obliczanie dni do następnych urodzin
        if "birthday" in self.fields:
            today = datetime.now()

            if isinstance(self.fields["birthday"][0].value, str):
                birthday_date = datetime.strptime(
                    self.fields["birthday"][0].value, '%Y-%m-%d')
            else:
                birthday_date = self.fields["birthday"][0].value

            next_birthday = datetime(
                today.year + 1, birthday_date.month, birthday_date.day)
            days_left = (next_birthday - today).days
            return days_left if days_left > 0 else 365 + days_left

    def __str__(self):
        # Tworzenie ciągu znaków opisujących pola rekordu
        fields_str = ", ".join(
            f"{field}: {getattr(self.fields[field], 'value', '')}" for field in self.fields)
        # Zwracanie sformatowanego ciągu znaków zawierających imię i pola
        return f"Name: {self.name.value}, {fields_str}"

# Klasa dziedzicząca po UserDict, reprezentująca książkę adresową


class AddressBook(UserDict):
    def add_record(self, record):
        # Dodawanie nowego rekordu do książki adresowej
        unique_key = record.name.value
        self.data[unique_key] = record

    def search_records(self, criteria):
        # Wyszukiwanie rekordów na podstawie określonych kryteriów
        matching_records = []
        for record in self.data.values():
            matches_criteria = any(
                (field == 'name' and getattr(record.name, 'value', None) and criteria[field].lower() in record.name.value.lower()) or
                (field in record.fields and (
                    (isinstance(record.fields[field], list) and any(criteria[field].lower() in f.value.lower() for f in record.fields[field] if hasattr(f, 'value'))) or
                    (not isinstance(
                        record.fields[field], list) and criteria[field].lower() in record.fields[field][0].value.lower())
                ))
                for field in criteria.keys()
            )
            if matches_criteria:
                matching_records.append(record)
        return matching_records

    def search(self, query):
        # Wyszukiwanie rekordów na podstawie ogólnego zapytania
        criteria = {
            "name": query,
            "phones": query,
            "emails": query,
            "birthday": query,
        }
        return self.search_records(criteria)

    def upcoming_birthdays(self, days):
        # Znajdowanie rekordów z nadchodzącymi urodzinami
        today = datetime.now()
        upcoming_birthdays_list = []

        for record in self.data.values():
            if "birthday" in record.fields:
                # Sprawdzamy dni do urodzin
                days_to_birthday = record.days_to_birthday()

                if 0 <= days_to_birthday <= days:
                    upcoming_birthdays_list.append(record)

        return upcoming_birthdays_list
