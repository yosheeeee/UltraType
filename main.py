#!/usr/bin/python3
import sys
import types

from design import Ui_MainWindow 
from PySide6.QtWidgets import QApplication, QMainWindow, QLineEdit
from PySide6.QtCore import QEvent, Qt

def keyPressEvent(self, keyEvent):
    letter = keyEvent
    if letter.key() not in (Qt.Key.Key_Shift, Qt.Key.Key_Escape):
        window.replace_letter(letter.text())
    if letter.key() == (Qt.Key.Key_Backspace):
        window.remove_letter()

class Ultratype(QMainWindow):
    def __init__(self):
        super(Ultratype, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.temp = self.ui.lbl_temp
        self.entry = self.ui.ln_entry
        self.final_text = 'The quick brown fox jumps over the lazy dog'

        self.entry.keyPressEvent = types.MethodType(keyPressEvent, QLineEdit)


    def get_entry_text(self):
        return (self.entry.text())

    def set_entry_text(self, text):
        self.entry.setText(str(text))
    
    def replace_letter(self, letter):
        position = self.entry.cursorPosition()
        replaced_text = self.get_entry_text()[:position] + letter + self.get_entry_text()[position + 1:]
        self.set_entry_text(replaced_text)
        self.entry.setCursorPosition(position+1)

    def remove_letter(self):
        position = self.entry.cursorPosition() -1 
        replaced_text = self.get_entry_text()[:position - 1] + self.final_text[position - 1:]
        print(self.entry.cursorPosition() - 1)
        print(position != 0)
        if (position != 0):
            self.set_entry_text(replaced_text)
            self.entry.setCursorPosition(position - 1)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Ultratype()
    window.set_entry_text(window.final_text)
    window.entry.setCursorPosition(0)
    window.show()

    sys.exit(app.exec())
