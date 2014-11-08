__author__ = 'Zaycev Denis'


import re
import math


not_russian_letter = re.compile("[^а-яА-Я]")


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

    def get_weight(self, count, negative_total, positive_total):
        if self.positive_count == 0 and self.negative_count == 0:
            return 0
        elif self.negative_count == 0:
            return count * math.log2((negative_total * self.positive_count) / positive_total)

        sign = 1
        if self.positive_count < self.negative_count:
            sign = -1

        value = (negative_total * self.positive_count) / (positive_total * self.negative_count)
        return sign * count * math.log2(value) if value != 0 else 0


def process_word(line):
    return not_russian_letter.sub('', line).lower()


def get_mapping(file_name, mapping=None):
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

        for chunk in chunks[2].split(' '):
            chunk = process_word(chunk)
            if len(chunk) == 0:
                continue

            value = mapping.get(chunk)
            if value is None:
                value = SentimentCounter()
                mapping[chunk] = value

            value.add(positive_rate, negative_rate)

    file.close()

    return positive_count, neutral_count, neutral_count, mapping
