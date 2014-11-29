__author__ = 'Zaycev Denis'

from src.util.common import get_words, sigmoid
from src.util.sentiment_estimation import SentimentCounter
from src.util.sentiment_estimation import MORPH
from src.util.spell_checker import correct


DEFAULT_SENTIMENT_COUNTER = SentimentCounter()


def process(sentence, estimated_words, known_words):
    corrected_words = []
    for word in get_words(sentence):
        corrected_words.append(correct(word, known_words))

    words_map = {}
    for word in corrected_words:
        word = MORPH.parse(correct(word, known_words))[0].normal_form
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
