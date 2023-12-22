import csv
import argparse

parser = argparse.ArgumentParser(description='Take notes while watching a video.')

parser.add_argument('-w', '--Write', help = 'Start writing notes.')
parser.add_argument('-d', '--Delete', help = 'Delete a single note.')
parser.add_argument('-a', '--Add', help = 'Add a single note.')
parser.add_argument('-p', '--Print', help = 'Print the notes.')
parser.add_argument('-e', '--Edit', help = 'Edit a note.')

args = parser.parse_args()

note_list = []

class Note:
    def __init__(self, timecode, content):
        self.timecode = timecode    # Timecode of the note
        self.content = content  # Content of the note (string)

    def __str__(self):
        return f"Note: timecode={self.timecode}, content={self.content}"

def export_notes(note_list):
    sort_notes(note_list)
    with open('book.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for note in note_list:
            writer.writerow([note.timecode, note.content])

def import_notes(note_list):
    note_list = []
    with open('book.csv', newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            note_list.append(Note(row[0], row[1]))

def sort_notes(note_list):
    for note in note_list:
        note.timecode = float(note.timecode)
    note_list.sort(key=lambda note: note.timecode)

def start_taking_notes(note_list):
    print('Type "exit" to stop taking notes.')
    movietime = 0  # Timecode of the note. Will implement later.
    while True:
        content = input('Note: ')
        if content == 'exit':
            break
        note = Note(movietime, content)
        note_list.append(note)
    return note_list

def print_notes(note_list):
    for note in note_list:
        print(f'Note #{note.index()}:\n{note.timecode}: {note.content}')

def edit_notes(note_list):
    print_notes(note_list)
    id = input('Which note do you want to edit?')
    pass

if args.Write:
    import_notes()
    start_taking_notes(note_list)
    export_notes(note_list)