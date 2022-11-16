#!/usr/bin/python3
import sys

from design import Ui_MainWindow
from labeledit import LabelEdit
from PySide6.QtWidgets import QApplication, QMainWindow, QLineEdit, QLabel
from PySide6.QtCore import Qt

class Ultratype(QMainWindow):

    def __init__(self):
        super(Ultratype, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.temp = self.ui.lbl_temp
        self.entry = self.ui.lbl_entry

        self.entry.final_text = 'The quick brown fox jumps over the lazy dog'
        self.entry.final_text_array = self.entry.str_to_array(self.entry.final_text)
        self.entry.current_text_array = self.entry.str_to_array(self.entry.final_text)
        print(self.entry.current_text_array)

    def keyPressEvent(self, keyEvent):
        letter = keyEvent
        if self.entry.check_key(letter):
            self.entry.replace_letter(letter.text())
        elif (letter.key() == Qt.Key.Key_Space):
            self.entry.replace_letter(letter.text())
        elif (letter.key() == Qt.Key.Key_Backspace) and (self.entry.current_position > 0):
            self.entry.remove_letter()

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Ultratype()
    window.entry.set_entry_text(window.entry.final_text)
    window.show()

    sys.exit(app.exec())
