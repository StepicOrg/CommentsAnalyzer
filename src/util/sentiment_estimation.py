__author__ = 'Zaycev Denis'


import math
import collections
from src.util.common import get_words
from src.util.spell_checker import correct


SEPARATOR = '\t'


class SentimentCounter:
    def __init__(self):
        self.neutral_count = 0
        self.positive_count = 0
        self.negative_count = 0

    def add(self, positive_estimation, negative_estimation):
        if positive_estimation > negative_estimation:
            self.positive_count += 1
        elif positive_estimation < negative_estimation:
            self.negative_count += 1
        else:
            self.neutral_count += 1

    def get_weight(self, negative_total, positive_total):
        if self.positive_count == 0 and self.negative_count == 0:
            return 0
        elif self.negative_count == 0:
            return math.log2((negative_total * self.positive_count) / positive_total)

        sign = 1
        if self.positive_count < self.negative_count:
            sign = -1

        value = (negative_total * self.positive_count) / (positive_total * self.negative_count)
        return sign * math.log2(value) if value != 0 else 0


def save_known_sentiment(file_name, negative, neutral, positive, mapping):
    """
    " Use this function to save prepared
    " known_sentiments.
    """
    file = open(file_name, "w", encoding='utf-8')
    for word, s_c in mapping.items():
        file.write(word + SEPARATOR + str(s_c.get_weight(negative, positive)) + '\n')

    file.close()


def load_known_sentiments(file_name):
    """
    " Use this function if you already prepare
    " known_sentiments to load.
    """
    model = collections.defaultdict(lambda: 1)

    file = open(file_name, "r", encoding='utf-8')
    for line in file.readlines():
        data = line.split(SEPARATOR)
        model[data[0]] = float(data[1])

    file.close()

    return model


def get_mapping(file_name, known_word, mapping=None):
    if not mapping:
        mapping = {}

    neutral_count = 0
    positive_count = 0
    negative_count = 0

    file = open(file_name, "r", encoding='utf-8')

    lines = file.readlines()
    for line in lines:

        chunks = line.split('\t')
        if len(chunks) != 3:
            continue

        positive_rate = int(chunks[0])
        negative_rate = int(chunks[1])

        neutral_count += 1 if positive_rate == negative_rate else 0
        positive_count += 1 if positive_rate > negative_rate else 0
        negative_count += 1 if positive_rate < negative_rate else 0

        for word in get_words(chunks[2]):
            word = correct(word, known_word)

            value = mapping.get(word)
            if value is None:
                value = SentimentCounter()
                mapping[word] = value

            value.add(positive_rate, negative_rate)

    file.close()

    return positive_count, neutral_count, neutral_count, mapping
