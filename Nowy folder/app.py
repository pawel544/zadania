from logic import *

from address_book import *

def execute_command(command, address_book, note_collection):
    if command == "help":
        print("""
        "help" - wywołuje listę komend,
        "hello" - wywołuje powitalny komunikat,
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

    elif command == "hello":
        print("Hello! Welcome to the address book and notepad application.")

    elif command == "add":
        add_contact(address_book)

    elif command == "change":
        change_contact(address_book)

    elif command == "show all":
        show_all_contacts(address_book)
    elif command == "find_note":
        find_note_by_title(note_collection)
    elif command == "delete_contact":
        delete_contact(address_book)

    elif command == "display_birthday":
        display_birthdays(address_book)

    elif command == "add_note":
        add_note(note_collection)

    elif command == "add_tag":
        add_tag_to_note(note_collection)

    elif command == "find_note":
        find_note_by_title(note_collection)

    elif command == "find_by_tag":
        find_note_by_tag(note_collection)

    elif command == "edit_note":
        edit_note(note_collection)

    elif command == "delete_note":
        delete_note_by_title(note_collection)

    elif command == "display_notes":
        display_notes(note_collection)

    elif command == "sort_notes":
        sort_notes_by_tag(note_collection)

    elif command.lower() in ["exit", "close"]:
        print("Exiting the application.")
        exit()

    else:
        print("Unknown command. Type 'help' to see the list of commands.")


def main():
    address_book = AddressBook()
    note_collection = NoteCollection()

    while True:
        user_input = input("Enter a command (type 'help' for a list of commands): ")
        execute_command(user_input, address_book, note_collection)


if __name__ == "__main__":
    main()