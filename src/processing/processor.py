__author__ = 'Zaycev Denis'

from src.util.common import get_words, sigmoid
from src.util.mapping import SentimentCounter


DEFAULT_SENTIMENT_COUNTER = SentimentCounter()


def process(sentence, estimated_words, positive_total, negative_total):
    words_map = {}
    for word in get_words(sentence):
        if word not in words_map:
            words_map[word] = 0
        words_map[word] += 1

    weights_map = {}
    for word, count in words_map.items():
        sentiment_counter = estimated_words.get(word, DEFAULT_SENTIMENT_COUNTER)
        weights_map[word] = sentiment_counter.get_weight(count, positive_total, negative_total)

    x = 0
    for word in get_words(sentence):
        x += weights_map[word]

    print(sigmoid(x))
