class LanguageModel:
    def __init__(self, label, known_letters):
        self.label = label
        self.known_letters = known_letters

    def get_label(self):
        return self.label

    def get_known_letters(self):
        return self.known_letters


# Predefined language models goes below
RUSSIAN = LanguageModel('Russian', 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ')
ENGLISH = LanguageModel('English', 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')