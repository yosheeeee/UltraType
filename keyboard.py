from PySide6.QtWidgets import QWidget
import config


class Keyboard(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    # Изменяет раскладку на виртуальной клавиатуре
    def set_keyboard_layout(self, keyboard_parent_object, buttons: str):
        button_number = 0
        for btn in config.KEYBOARD_BUTTONS:
            getattr(keyboard_parent_object, btn).setText(
                buttons[button_number])
            button_number += 1

    # Меняет цвет у кнопки 
    def highlight_button(self, button):
        button.setStyleSheet("background-color: #68627A")

    # Возвращает первоначальный цвет кнопке 
    def unhighlight_button(self, button):
        button.setStyleSheet("background-color: #302D38")
