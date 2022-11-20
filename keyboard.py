from PySide6.QtWidgets import QWidget
import config

class Keyboard(QWidget):
    def __init__(self, parent):
        super(Keyboard, self).__init__(parent)

    def set_keyboard_layout(self, keyboard_parent_object, buttons: str):
        button_number = 0
        for btn in config.KEYBOARD_BUTTONS:
            getattr(keyboard_parent_object, btn).setText(buttons[button_number])
            button_number += 1
