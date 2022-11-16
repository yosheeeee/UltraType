#!/usr/bin/python3
import sys
import types

from design import Ui_MainWindow 
from PySide6.QtWidgets import QApplication, QMainWindow, QLineEdit
from PySide6.QtCore import QEvent, Qt

class LineEdit(QLineEdit):
    def __init__(self):
        super(LineEdit, self).__init__()
        self.final_text = ''

    def keyPressEvent(self, keyEvent):
        letter = keyEvent
        if letter.key() not in (Qt.Key.Key_Shift, Qt.Key.Key_Escape, Qt.Key.Key_Backspace):
            self.replace_letter(letter.text())
        if letter.key() == (Qt.Key.Key_Backspace) and self.cursorPosition() > 0:
            self.remove_letter()

    def replace_letter(self, letter):
        position = self.cursorPosition()
        replaced_text = self.get_entry_text()[:position] + letter + self.get_entry_text()[position + 1:]
        self.set_entry_text(replaced_text)
        self.setCursorPosition(position+1)

    def remove_letter(self):
        position = self.cursorPosition() -1 
        replaced_text = self.get_entry_text()[:position] + self.final_text[position:]
        print(replaced_text)
        if (position != 0):
            self.set_entry_text(replaced_text)
            self.setCursorPosition(position)

    def get_entry_text(self):
        return (self.text())

    def set_entry_text(self, text):
        self.setText(str(text))
    
class Ultratype(QMainWindow):
    def __init__(self):
        super(Ultratype, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.temp = self.ui.lbl_temp
        self.ui.ln_entry.__class__ = LineEdit
        self.entry = self.ui.ln_entry
        self.entry.final_text = 'The quick brown fox jumps over the lazy dog'

        # self.entry.keyPressEvent = types.MethodType(keyPressEvent, QLineEdit)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Ultratype()
    window.entry.set_entry_text(window.entry.final_text)
    window.entry.setCursorPosition(0)
    window.show()

    sys.exit(app.exec())
