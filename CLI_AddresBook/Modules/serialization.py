import json
from .notebook import *
from main import *


def format_birthday(birthday):
    return str(birthday.value) if birthday else None


def to_json_address_book(filename, address_book):
    data = {
        name: {
            'name': record.name.value,
            'phone': [phone.value for phone in record.fields.get('phones', [])],
            'email': [email.value for email in record.fields.get('emails', [])],
            'birthday': format_birthday(record.fields.get('birthday', [None])[0]),
        }
        for name, record in address_book.data.items()
    }
    with open(filename, 'w') as data_file:
        json.dump(data, data_file, indent=2)


def from_json_address_book(filename):
    with open(filename, 'r') as data_file:
        data = json.load(data_file)
        records = {}

        for name, record_data in data.items():

            birthday = record_data.get('birthday', None)

            record = Record(
                name,
                birthday,
            )

            for phone_number in record_data.get('phone', []):
                record.add_field("phones", phone_number)

            for email_address in record_data.get('email', []):
                record.add_field("emails", email_address)

            records[name] = record

        return AddressBook(records)


def to_json_note(note, filename):
    notepad_data = {
        "notes": [
            {
                "title": note.title,
                "text": note.text,
                "tags": list(note.tags)
            }
            for note in note.notes
        ]
    }
    with open(filename, 'w') as data_file:
        json.dump(notepad_data, data_file, indent=2)


def from_json_note(filename):
    with open(filename, 'r') as data_file:
        data = json.load(data_file)
        notes = []
        for note_data in data.get('notes', []):
            note = Note(note_data.get('title', ''), note_data.get('text', ''))
            note.tags = set(note_data.get('tags', []))
            notes.append(note)
        note = NoteCollection()
        note.notes = notes
        return note
