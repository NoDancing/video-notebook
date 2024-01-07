import unittest
import os
from unittest.mock import patch
from video_notebook1 import Notebook, Note

class TestNotebook(unittest.TestCase):
    def setUp(self):
        self.notebook = Notebook()
    
    @patch('builtins.input', side_effect=['test', 'exit'])
    def test_start_taking_notes(self, mock_input):
        self.notebook.start_taking_notes()
        self.assertEqual(self.notebook.note_list[0].content, 'test')
        self.assertEqual(len(self.notebook.note_list), 1)
        self.assertEqual(self.notebook.note_list[0].timecode, 0)

    def test_print_notes(self):
        self.notebook.note_list = [Note(0, 'test')]
        with patch('builtins.print') as mock_print:
            self.notebook.print_notes()
            mock_print.assert_called_with('Note #0:\n0: test\n')
    
    @patch('builtins.input', side_effect=['0', 'test', 'n'])

    def test_edit_notes(self, mock_input):
        self.notebook.note_list = [Note(0, 'test')]
        self.notebook.edit_notes()
        self.assertEqual(self.notebook.note_list[0].content, 'test')
        self.assertEqual(len(self.notebook.note_list), 1)
        self.assertEqual(self.notebook.note_list[0].timecode, 0)
    
    def test_export_notes(self):
        self.notebook.note_list = [Note(0, 'test')]
        self.notebook.export_notes('test.csv')
        with open('test.csv', 'r') as file:
            self.assertEqual(file.read(), '0.0,test\n')
        os.remove('test.csv')
    
    def test_import_notes(self):
        with open('test.csv', 'w') as file:
            file.write('0.0,test\n')
        self.notebook.import_notes('test.csv')
        self.assertEqual(self.notebook.note_list[0].content, 'test')
        self.assertEqual(len(self.notebook.note_list), 1)
        self.assertEqual(self.notebook.note_list[0].timecode, 0.0)
        os.remove('test.csv')
    
if __name__ == '__main__':
    unittest.main()