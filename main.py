#!/usr/bin/python3
import sys

from design import Ui_MainWindow
from PySide6.QtWidgets import QApplication, QMainWindow, QLineEdit
from PySide6.QtCore import QEvent

class Ultratype(QMainWindow):
    def __init__(self):
        super(Ultratype, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.temp = self.ui.lbl_temp
        self.entry = self.ui.ln_entry
        self.final_text = 'The quick brown fox jumps over the lazy dog'

    def get_entry_text(self):
        return (self.entry.text())

    def set_entry_text(self, text):
        self.entry.setText(str(text))
        self.entry.setCursorPosition(0)
    
    def replace_letter(self, letter):
        position = self.entry.cursorPosition()
        replaced_text = text[:position] + letter + text[position + 1:]


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Ultratype()
    window.set_entry_text(window.final_text)
    window.show()

    sys.exit(app.exec())
