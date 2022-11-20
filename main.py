#!/usr/bin/python3
import sys
from time import sleep
import threading

from design import Ui_MainWindow
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import Qt
import config

class Ultratype(QMainWindow):

    def __init__(self):
        super(Ultratype, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.wpm = self.ui.lbl_wpm
        self.accuracy = self.ui.lbl_accuracy
        self.entry = self.ui.lbl_entry
        self.keyboard = self.ui.wt_keyboard
        self.wpm_thread = threading.Thread(target=self.stats_thread)


    def closeEvent(self, *args, **kwargs):
            super(QMainWindow, self).closeEvent(*args, **kwargs)
            self.wpm_thread.do_run = False

    def keyPressEvent(self, keyEvent):
        if not(self.entry.is_started):
            self.entry.start()
        letter = keyEvent
        if self.entry.check_key(letter):
            self.entry.replace_letter(letter.text())
        elif (letter.key() == Qt.Key.Key_Shift):
            self.keyboard.set_keyboard_layout(self.ui, config.ENG_LETTER_BUTTONS['upper'])
        elif (letter.key() == Qt.Key.Key_Space):
            self.entry.replace_letter(letter.text())
        elif (letter.key() == Qt.Key.Key_Backspace) and (self.entry.current_position > 0):
            self.entry.remove_letter()

    def keyReleaseEvent(self, keyEvent):
        letter = keyEvent
        if (letter.key() == Qt.Key.Key_Shift):
            self.keyboard.set_keyboard_layout(self.ui, config.ENG_LETTER_BUTTONS['lower'])

    def set_test_text(self, text):
        self.entry.final_text = text
        self.entry.final_text_array = self.entry.str_to_array(self.entry.final_text)
        self.entry.current_text_array = self.entry.str_to_array(self.entry.final_text)
        self.entry.set_entry_text(text)

    def stats_thread(self):
        thread = threading.current_thread()
        while getattr(thread, "do_run", True):
            sleep(0.2)
            self.wpm.set_wpm(self.wpm.calculate_wpm(self.entry.current_position, self.entry.start_time))
            self.accuracy.set_accuracy(self.wpm.calculate_accuracy(self.entry.entered_symbols_counter, self.entry.missed_symbols_counter))


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Ultratype()
    window.show()
    window.set_test_text('привет пока ты красавчик вообще лютейший')
    window.keyboard.current_keyboard_string = 'ENG_LETTER_BUTTONS'
    window.wpm_thread.start()
    sys.exit(app.exec())
