__author__ = 'Zaycev Denis'

from src.util.common import sigmoid


def process(text, estimated_words, text_parser):
    corrected_words = text_parser.correct_all_words(text_parser.get_words(text))

    words_map = {}
    for word in corrected_words:
        if word not in words_map:
            words_map[word] = 0

        words_map[word] += 1

    weights_map = {}
    for word, count in words_map.items():
        weight = estimated_words.get(word, 0)
        weights_map[word] = count * weight

    x = 0
    for word in corrected_words:
        x += weights_map[word]

    print(sigmoid(x))
