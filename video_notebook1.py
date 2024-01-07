import csv
import argparse

parser = argparse.ArgumentParser(description='Take notes while watching a video.')

parser.add_argument('-w', '--Write', action='store_true', help = 'Start writing notes.')
parser.add_argument('-d', '--Delete', action='store_true', help = 'Delete a single note.')
parser.add_argument('-a', '--Add', action='store_true', help = 'Add a single note.')
parser.add_argument('-p', '--Print', action='store_true', help = 'Print the notes.')
parser.add_argument('-e', '--Edit', action='store_true', help = 'Edit a note.')

args = parser.parse_args()

note_list = []

CSV_FILE = 'notes.csv'

class Note:
    """A note that contains timecode and content."""
    def __init__(self, timecode, content):
        self.timecode = timecode    # Timecode of the note
        self.content = content  # Content of the note (string)

    def __str__(self):
        return f"Note: timecode={self.timecode}, content={self.content}"

class Notebook:
    def __init__(self):
        self.note_list = []

    def import_notes(self, CSV_FILE):
        """Reads notes from a csv file and adds them to the notebook as a list."""
        with open(CSV_FILE, 'r', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                timecode = float(row[0])
                self.note_list.append(Note(timecode, row[1]))

    def sort_notes(self):
        """Sorts the notes by timecode."""
        for note in self.note_list:
            note.timecode = float(note.timecode)
        self.note_list.sort(key=lambda note: note.timecode)

    def start_taking_notes(self):
        """Starts the note-taking input loop."""
        print('Type "exit" to stop taking notes.')
        movietime = 0  # Timecode of the note. Will implement later.
        while True:
            content = input('Note: ')
            if content == 'exit':
                break
            note = Note(movietime, content)
            self.note_list.append(note)

    def print_notes(self):
        """Prints every note sequentially with timecode and list index."""
        for note in self.note_list:
            print(f'Note #{self.note_list.index(note)}:\n{note.timecode}: {note.content}\n')

    def edit_notes(self):
        """Prints all notes, replaces chosen note with new content."""
        while True:
            self.print_notes()
            id = int(input('Which note do you want to edit?'))
            self.note_list[id].content = input('New content: ')
            continue_editing = input("Enter y to edit another note: ")
            if continue_editing != 'y':
                break

    def export_notes(self, CSV_FILE):
        """Writes the notes in the notebook to a csv file."""
        self.sort_notes()
        with open(CSV_FILE, 'w', newline='') as file:
            writer = csv.writer(file)
            for note in self.note_list:
                writer.writerow([note.timecode, note.content])

    def add_note(self):
        """Adds a single note to the notebook with a timecode of 0."""
        content = input('New Content: ')
        note = Note(0, content)
        self.note_list.append(note)

    def delete_notes(self):
        """Prints all notes and deletes the selected note."""
        while True:
            self.print_notes()
            id = int(input('Which note do you want to delete? '))
            self.note_list.pop(id)
            continue_editing = input("Enter y to delete another note: ")
            if continue_editing != 'y':
                break



notebook = Notebook()
notebook.import_notes(CSV_FILE)

if args.Write:
    notebook.start_taking_notes()

if args.Print:
    notebook.print_notes()

if args.Edit:
    notebook.edit_notes()

if args.Add:
    notebook.add_note()

if args.Delete:
    notebook.delete_notes()

notebook.export_notes(CSV_FILE)
