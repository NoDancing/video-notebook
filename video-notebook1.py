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

csvfile = 'notes.csv'

class Note:
    def __init__(self, timecode, content):
        self.timecode = timecode    # Timecode of the note
        self.content = content  # Content of the note (string)

    def __str__(self):
        return f"Note: timecode={self.timecode}, content={self.content}"

class Notebook:
    def __init__(self):
        self.note_list = []

    def import_notes(self, csvfile):
        with open(csvfile, 'r', newline='') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                self.note_list.append(Note(row[0], row[1]))

    def sort_notes(self):
        for note in self.note_list:
            note.timecode = float(note.timecode)
        self.note_list.sort(key=lambda note: note.timecode)

    def start_taking_notes(self):
        print('Type "exit" to stop taking notes.')
        movietime = 0  # Timecode of the note. Will implement later.
        while True:
            content = input('Notes: ')
            if content == 'exit':
                break
            note = Note(movietime, content)
            self.note_list.append(note)

    def print_notes(self):
        for note in self.note_list:
            print(f'Note #{self.note_list.index(note)}:\n{note.timecode}: {note.content}')

    def edit_notes(self):
        self.print_notes()
        id = input('Which note do you want to edit?')
        # implement editing logic here
    
    def export_notes(self, csvfile):
        self.sort_notes()
        with open(csvfile, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            for note in self.note_list:
                writer.writerow([note.timecode, note.content])

if args.Write:
    notebook = Notebook()
    notebook.import_notes(csvfile)
    notebook.start_taking_notes()
    notebook.export_notes(csvfile)

if args.Print:
    notebook = Notebook()
    notebook.import_notes(csvfile)
    notebook.print_notes()

