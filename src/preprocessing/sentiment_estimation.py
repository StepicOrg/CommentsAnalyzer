__author__ = 'Zaycev Denis'

import math
import collections


SEPARATOR = '\t'


POSITIVE_TONALITY = 'pos'
NEUTRAL_TONALITY = 'neu'
NEGATIVE_TONALITY = 'neg'


def calculate_weights(data_set, text_parser):
    lines_processed = 0

    total = [0, 0, 0]
    words_count = collections.defaultdict(lambda : [0, 0, 0])
    for data in data_set:
        chunks = data.split(SEPARATOR)   # [tonality, text]

        total[get_index_by_key(chunks[0])] += 1

        words = text_parser.correct_all_words(text_parser.get_words(chunks[1]))
        for word in words:
            words_count[word][get_index_by_key(chunks[0])] += 1

        for pair in text_parser.get_words_pairs(words):
            words_count[pair][get_index_by_key(chunks[0])] += 1

        lines_processed += 1
        print("Lines processed: " + str(lines_processed))

    weights = collections.defaultdict(lambda : 1)
    for word, count in words_count.items():
        if words_count[word][get_index_by_key(POSITIVE_TONALITY)] == 0 \
                or words_count[word][get_index_by_key(NEGATIVE_TONALITY)] == 0:
            continue

        # multipliers for delta TF-IDF algorithm
        weights[word] = math.log(
            total[get_index_by_key(NEGATIVE_TONALITY)] * words_count[word][get_index_by_key(POSITIVE_TONALITY)]
            / total[get_index_by_key(POSITIVE_TONALITY)] / words_count[word][get_index_by_key(NEGATIVE_TONALITY)])

    return weights


def get_index_by_key(key):
    if NEGATIVE_TONALITY == key:
        return 0

    if NEUTRAL_TONALITY == key:
        return 1

    return 2