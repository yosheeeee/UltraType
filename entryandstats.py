from time import time
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QLabel


class LabelEdit(QLabel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.final_text = ''
        self.current_text_array = []
        self.final_text_array = []
        self.current_position = 0
        self.entered_symbols_counter = 0
        self.missed_symbols_counter = 0
        self.is_started = False
        self.start_time = 0
    
    # Функция запускающая таймер
    def start(self):
        self.start_time = time()
        self.is_started = True

    # Проверяет является ли буква полученная на вход подходящей
    @staticmethod
    def check_key(letter):
        return (letter.text().isalnum() or
                letter.key() == Qt.Key.Key_Colon or
                letter.key() == Qt.Key.Key_Semicolon or
                letter.key() == Qt.Key.Key_Comma or
                letter.key() == Qt.Key.Key_Apostrophe or
                letter.key() == Qt.Key.Key_Exclam or
                letter.key() == Qt.Key.Key_Question or
                letter.key() == Qt.Key.Key_BraceLeft or
                letter.key() == Qt.Key.Key_BraceRight or
                letter.key() == Qt.Key.Key_BracketLeft or
                letter.key() == Qt.Key.Key_BracketRight or
                letter.key() == Qt.Key.Key_QuoteDbl or
                letter.key() == Qt.Key.Key_Period)
    
    # Преобразует массив в строку и возвращает полученную строку
    @staticmethod
    def array_to_str(str):
        return ''.join(str)

    # Преобразует строку в массив и возвращает полученную массив
    @staticmethod
    def str_to_array(str):
        return [char for char in str]

    # Сверяет два символа полученных на вход
    @staticmethod
    def letter_is_correct(letter, correct_letter):
        return letter == correct_letter

    # Добавляет букву в отображаемый текст, если вводимая буква правильная, то она имеет зеленый цвет, если нет, то красный 
    def replace_letter(self, letter):
        position = self.current_position
        if len(self.final_text_array) > position:
            final_text_letter = self.final_text_array[position]
            if self.letter_is_correct(letter, final_text_letter):
                self.current_text_array[
                    position] = f"<span style='color: green;'>{letter}</span>"
            else:
                if (final_text_letter==' '):
                    self.current_text_array[position]=f"<span style='text-decoration: underline !important; text-decoration-color:red !important;'>{final_text_letter}</span>"
                else:
                    self.current_text_array[
                        position] = f"<span style='color: red'>{final_text_letter}</span>"
                self.missed_symbols_counter += 1
            self.set_entry_text(self.array_to_str(self.current_text_array))
            self.entered_symbols_counter += 1
            self.current_position += 1
            self.set_underline_letter(self.current_position)

    # Добавляет курсор под текущий символ
    def set_underline_letter(self, position):
        if (position < len(self.final_text_array)):
            self.current_text_array[
                position] = f"<span style='text-decoration: underline !important;'>{self.final_text_array[position]}</span>"
            self.set_entry_text(self.array_to_str(self.current_text_array))

    # Удаляет курсор с текущего символа
    def remove_underline_letter(self, position):
        if (position < len(self.final_text_array)):
            self.current_text_array[
                position] = f"<span style='text-decoration: none;'>{self.final_text_array[position]}</span>"
            self.set_entry_text(self.array_to_str(self.current_text_array))

    # Удаляет букву из отображаемого текста
    def remove_letter(self):
        position = self.current_position
        if position > 0:
            self.remove_underline_letter(position)
            position -= 1
            self.current_text_array[position] = self.final_text_array[position]
            self.set_entry_text(self.array_to_str(self.current_text_array))
            self.set_underline_letter(position)
            self.current_position -= 1

    # Возвращает отображаемый текст
    def get_entry_text(self):
        return (self.text())

    # Задает отображаемый текст
    def set_entry_text(self, text):
        self.setText(str(text))


class LabelStat(QLabel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    # Высчитывает WPM
    @staticmethod
    def calculate_wpm(text_len, start_time):
        time_elapsed = max(time() - start_time, 1)
        wpm = round(text_len / (time_elapsed / 60) / 5)
        return wpm

    # Высчитывает точность
    @staticmethod
    def calculate_accuracy(entered_symbols, missed_symbols):
        if entered_symbols > 0:
            accuracy = round(100 - ((missed_symbols * 100) / entered_symbols))
            return accuracy
        else:
            return 0

    # Задает текст WPM
    def set_wpm(self, wpm):
        self.setText(f'WPM {wpm}')

    # Задает текст точности
    def set_accuracy(self, accuracy):
        self.setText(f'Accuracy {accuracy}%')
