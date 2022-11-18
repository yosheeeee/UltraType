#!/usr/bin/python3
import sys

from design import Ui_MainWindow
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import Qt

class Ultratype(QMainWindow):

    def __init__(self):
        super(Ultratype, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.wpm = self.ui.lbl_wpm
        self.entry = self.ui.lbl_entry

        self.entry.final_text = 'The quick brown fox jumps over the lazy dog'
        self.entry.final_text_array = self.entry.str_to_array(self.entry.final_text)
        self.entry.current_text_array = self.entry.str_to_array(self.entry.final_text)

    def keyPressEvent(self, keyEvent):
        letter = keyEvent
        if self.entry.check_key(letter):
            self.entry.replace_letter(letter.text())
            self.wpm.set_wpm(self.wpm.calculate_wpm(self.entry.current_position, self.entry.start_time))
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
