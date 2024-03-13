class Note:
    def __init__(self, title, text):
        self.title = title
        self.text = text
        self.tags = set()

    def add_tag(self, tag):
        self.tags.add(tag)

    def __repr__(self):
        return (
            f"Note: {self.title}\n"
            f"Tags: {', '.join(self.tags)}\n"
            f"Content: {self.text}\n"
        )


class NoteCollection:
    def __init__(self):
        self.notes = []

    def add_note(self, note):
        self.notes.append(note)

    def search_notes_by_tag(self, tag):
        return [note for note in self.notes if tag in note.tags]

    def sort_notes_by_tag(self, tag):
        return sorted(self.notes, key=lambda note: tag in note.tags)

    def __repr__(self):
        return '\n\n'.join(map(str, self.notes))


class Notepad:
    def __init__(self):
        self.notes = []

    def add_note(self, title, text):
        new_note = Note(title, text)
        self.notes.append(new_note)
        return new_note

    def add_tag_to_note(self, note, tag):
        note.add_tag(tag)

    def find_note_by_title(self, title):
        for note in self.notes:
            if note.title == title:
                return note
        return None

    def edit_note_text(self, title, new_text):
        note = self.find_note_by_title(title)
        if note:
            note.text = new_text

    def delete_note_by_title(self, title):
        note = self.find_note_by_title(title)
        if note:
            self.notes.remove(note)

    def display_notes(self):
        for note in self.notes:
            print(f'Title of the note: {note.title}\n'
                  f'Tags: {", ".join(note.tags)}\n'
                  f'Text:\n{note.text}\n')