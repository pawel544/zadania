from main import *
from .notebook import *


def add_contact(address_book):
    name = input("Enter the name: ")
    phone = input("Enter the phone number: ")
    birthday = input("Enter the birthday (YYYY-MM-DD): ")
    email = input("Enter the email: ")

    record = Record(name, birthday=birthday)
    record.add_field("phones", phone)
    record.add_field("emails", email)

    address_book.add_record(record)
    print(f"Contact '{name}' added successfully.")


def change_contact(address_book):
    name_to_change = input("Enter the name of the contact to change: ")
    if name_to_change in address_book.data:
        record_to_change = address_book.data[name_to_change]

        # You can add logic to modify the contact details here

        print(f"Contact '{name_to_change}' has been changed.")
    else:
        print(f"Contact '{name_to_change}' not found.")


def show_all_contacts(address_book):
    for record in address_book.data.values():
        print(record)


def delete_contact(address_book):
    name_to_delete = input("Enter the name of the contact to delete: ")
    if name_to_delete in address_book.data:
        del address_book.data[name_to_delete]
        print(f"Contact '{name_to_delete}' has been deleted.")
    else:
        print(f"Contact '{name_to_delete}' not found.")


def display_birthdays(address_book):
    days = int(input("Enter the number of days for upcoming birthdays: "))
    upcoming_birthdays = address_book.upcoming_birthdays(days)

    if upcoming_birthdays:
        print(f"Upcoming birthdays in the next {days} days:")
        for record in upcoming_birthdays:
            print(record)
    else:
        print("No upcoming birthdays in the specified days.")


def add_note(note_collection):
    title = input("Enter the title of the note: ")
    text = input("Enter the text of the note: ")
    note = Note(title, text)

    note_collection.add_note(note)
    print("Note added successfully.")


def add_tag_to_note(note_collection):
    title = input("Enter the title of the note to add a tag: ")
    note = note_collection.find_note(title)

    if note:
        tag = input("Enter the tag to add: ")
        note.add_tag(tag)
        print(f"Tag '{tag}' added to the note '{title}'.")
    else:
        print(f"Note '{title}' not found.")


def find_note_by_title(note_collection):
    title = input("Enter the title of the note to find: ")
    note = note_collection.find_note(title)

    if note:
        print(note)
    else:
        print(f"Note '{title}' not found.")


def find_note_by_tag(note_collection):
    tag = input("Enter the tag to search for notes: ")
    matching_notes = note_collection.search_notes_by_tag(tag)

    if matching_notes:
        print(f"Notes with tag '{tag}':")
        for note in matching_notes:
            print(note)
    else:
        print(f"No notes found with tag '{tag}'.")


def edit_note(note_collection):
    title = input("Enter the title of the note to edit: ")
    note = note_collection.find_note(title)

    if note:
        new_text = input("Enter the new text for the note: ")
        note.text = new_text
        print(f"Note '{title}' has been edited.")
    else:
        print(f"Note '{title}' not found.")


def delete_note_by_title(note_collection):
    title = input("Enter the title of the note to delete: ")
    note = note_collection.find_note(title)

    if note:
        note_collection.notes.remove(note)
        print(f"Note '{title}' has been deleted.")
    else:
        print(f"Note '{title}' not found.")


def display_notes(note_collection):
    if note_collection.notes:
        print("List of notes:")
        for note in note_collection.notes:
            print(note)
    else:
        print("No notes available.")


def sort_notes_by_tag(note_collection):
    tag = input("Enter the tag to sort notes: ")
    sorted_notes = note_collection.sort_notes_by_tag(tag)

    if sorted_notes:
        print(f"Sorted notes with tag '{tag}':")
        for note in sorted_notes:
            print(note)
    else:
        print(f"No notes found with tag '{tag}'.")
