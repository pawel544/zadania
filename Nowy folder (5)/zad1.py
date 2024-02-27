from address_book import *
from abc import abstractmethod
from notebook import *
from logic import *
class UserRepresentation(ABC):
    @abstractmethod
    def display(self):
        pass

class ConsoleUserRepresentation(UserRepresentation):
    def display(self, data):
        print(data)

class CardUserRepresentation(UserRepresentation):
    def display(self, data):
         pass

class NotePageUserRepresentation(UserRepresentation):
    def display(self, data):
        pass




def help_command():
    print("""
    "help" - wywołuje listę komend,
    "hello" - wywołuje p owitalny komunikat,
    "add" - dodaje kontakt według podanego schematu: nazwa kontaktu, numer telefonu, email, data urodzin,
    "change" - zmienia nazwę kontaktu, numer telefonu, email i datę urodzin,
    "show all" - wyświetla wszystkie kontakty w książce kontaktów,
    "delete_contact" - usuwa kontakt,
    "display_birthday" - wyświetla listę kontaktów, których urodziny przypadają za określoną liczbę dni od bieżącej daty,
    "add_note" - dodaje notatkę,
    "add_tag" - dodaje tag do wybranej notatki,
    "find_note" - wyszukuje notatkę według tytułu,
    "find_by_tag" - wyszukuje notatkę według znacznika,
    "edit_note" - edytuje notatki,
    "delete_note" - usuwa notatki według tytułu,
    "display_notes" - wyświetla notatki,
    "sort_notes" - sortuje notatki według znacznika,
    "exit", "close" - zamyka książkę adresową
    """)

def hello_command():
    print("Hello! Welcome to the address book and notepad application.")

def main():
    address_book = AddressBook()
    note_collection = NoteCollection()

    commands = {
        "help": help_command,
        "hello": hello_command,
        "add": lambda: add_contact(address_book),
        "change": lambda: change_contact(address_book),
        "show all": lambda: show_all_contacts(address_book),
        "delete_contact": lambda: delete_contact(address_book),
        "display_birthday": lambda: display_birthdays(address_book),
        "add_note": lambda: add_note(note_collection),
        "add_tag": lambda: add_tag_to_note(note_collection),
        "find_note": lambda: find_note_by_title(note_collection),
        "find_by_tag": lambda: find_note_by_tag(note_collection),
        "edit_note": lambda: edit_note(note_collection),
        "delete_note": lambda: delete_note_by_title(note_collection),
        "display_notes": lambda: display_notes(note_collection),
        "sort_notes": lambda: sort_notes_by_tag(note_collection),
        "exit": lambda: exit("Exiting the application.")
    }

    while True:
        user_input = input("Enter a command (type 'help' for a list of commands): ")
        command = commands.get(user_input.lower())
        if command:
            command()
        else:
            print("Unknown command. Type 'help' to see the list of commands.")

if __name__ == "__main__":
    main()

