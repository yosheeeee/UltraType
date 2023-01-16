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
        self.stat_thread = threading.Thread(target=self.stats_thread)
        self.current_layout = config.ENG_LETTER_BUTTONS
        self.highlighted_button = None
        self.next_button_is_upper = None

    def closeEvent(self, *args, **kwargs):
            super(QMainWindow, self).closeEvent(*args, **kwargs)
            self.kill_threads()

    def kill_threads(self):
        self.stat_thread.do_run = False

    def current_letter_is_upper(self):
        return self.entry.final_text_array[self.entry.current_position] in self.current_layout['upper']

    def test_is_complete(self):
        if len(self.entry.final_text_array) > 0:
            return self.entry.current_position == len(self.entry.final_text_array)

    def get_current_button_id(self):
            letter = self.entry.final_text_array[self.entry.current_position]
            if letter == ' ':
                return self.ui.btn_space
            elif letter in self.current_layout['lower']:
                return getattr(self.ui, config.KEYBOARD_BUTTONS[self.current_layout['lower'].find(letter)])
            elif letter in self.current_layout['upper']:
                return getattr(self.ui, config.KEYBOARD_BUTTONS[self.current_layout['upper'].find(letter)])

    def keyPressEvent(self, keyEvent):
        self.handle_key(keyEvent)

    def handle_key(self, keyEvent):
        letter = keyEvent
        if self.entry.check_key(letter):
            if not(self.entry.is_started):
                self.entry.start()
            self.entry.replace_letter(letter.text())
        elif (letter.key() == Qt.Key.Key_Shift):
            self.keyboard.set_keyboard_layout(self.ui, config.ENG_LETTER_BUTTONS['upper'])
        elif (letter.key() == Qt.Key.Key_Space):
            self.entry.replace_letter(letter.text())
        elif (letter.key() == Qt.Key.Key_Backspace) and (self.entry.current_position > 0):
            self.entry.remove_letter()
        if self.test_is_complete():
            self.kill_threads()
        self.refresh_highlight()

    def keyReleaseEvent(self, keyEvent):
        letter = keyEvent
        if (letter.key() == Qt.Key.Key_Shift):
            self.keyboard.set_keyboard_layout(self.ui, config.ENG_LETTER_BUTTONS['lower'])
        self.refresh_highlight()

    def set_test_text(self, text):
        self.entry.final_text = text
        self.entry.final_text_array = self.entry.str_to_array(self.entry.final_text)
        self.entry.current_text_array = self.entry.str_to_array(self.entry.final_text)
        self.entry.set_entry_text(text)
        self.highlighted_button = self.get_current_button_id()

    def stats_thread(self):
        thread = threading.current_thread()
        while getattr(thread, "do_run", True):
            sleep(0.1)
            self.wpm.set_wpm(self.wpm.calculate_wpm(self.entry.current_position, self.entry.start_time))
            self.accuracy.set_accuracy(self.wpm.calculate_accuracy(self.entry.entered_symbols_counter, self.entry.missed_symbols_counter))

    def refresh_highlight(self):
        if len(self.entry.final_text_array) > self.entry.current_position:
            self.keyboard.highlight_button(self.get_current_button_id())
            if self.highlighted_button != self.get_current_button_id():
                self.keyboard.unhighlight_button(self.ui.btn_lshift)
                self.keyboard.unhighlight_button(self.highlighted_button)
                self.highlighted_button = self.get_current_button_id()
            if self.current_letter_is_upper():
                self.keyboard.highlight_button(self.ui.btn_lshift)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Ultratype()
    window.show()
    window.set_test_text("CIsnotbetrayal. What you say or do doesn't matter; only feelings matter.")
    window.entry.set_underline_letter(0)
    window.stat_thread.start()
    window.refresh_highlight()
    sys.exit(app.exec())
