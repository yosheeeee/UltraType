from PySide6.QtCore import Qt
from PySide6.QtWidgets import QLabel

class LabelEdit(QLabel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.final_text = ''
        self.current_text_array = []
        self.final_text_array = []
        self.current_position = 0

    @staticmethod
    def check_key(letter):
        return (letter.text().isalnum() or 
                letter.key() == Qt.Key.Key_Colon or 
                letter.key() == Qt.Key.Key_Semicolon)

    @staticmethod
    def array_to_str(str):
        return ''.join(str)

    @staticmethod
    def str_to_array(str):
        return [char for char in str]

    @staticmethod
    def letter_is_correct(letter, correct_letter):
        return letter == correct_letter


    def replace_letter(self, letter):
        position = self.current_position
        final_text_letter = self.final_text_array[position]
        if self.letter_is_correct(letter, final_text_letter):
            self.current_text_array[position] = f"<span style='color: green'>{letter}</span>"
        else:
            self.current_text_array[position] = f"<span style='color: red'>{final_text_letter}</span>"
        self.set_entry_text(self.array_to_str(self.current_text_array))
        self.current_position += 1
    
    def remove_letter(self):
        position = self.current_position - 1 
        self.current_text_array[position] = self.final_text_array[position]
        self.set_entry_text(self.array_to_str(self.current_text_array))
        self.current_position -= 1

    def get_entry_text(self):
        return (self.text())

    def set_entry_text(self, text):
        self.setText(str(text))
    
