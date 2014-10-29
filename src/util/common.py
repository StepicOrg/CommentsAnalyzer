import re
import math

NOT_RUSSIAN_LETTER = re.compile("[^а-яА-Я]")


def clear_sentence(sentence):
    return NOT_RUSSIAN_LETTER.sub(' ', sentence).lower().strip()


def get_words(sentence):
    words = []
    for word in clear_sentence(sentence).split(' '):
        if not word:
            continue

        words.append(word)

    return words

def sigmoid(x):
    return  1 / (1 + math.pow(x, -math.e))