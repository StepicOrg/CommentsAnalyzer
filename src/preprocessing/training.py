__author__ = 'Zaycev Denis'

import collections

from src.preprocessing.sentiment_estimation import calculate_weights
from src.util.ai.machine_learning import get_words_features
from src.util.ai.model import Model
from sklearn.naive_bayes import GaussianNB


class Teacher:
    def __init__(self, comments, answers, text_parser):
        self.comments = comments
        self.answers = answers
        self.text_parser = text_parser

        # To be prepared while training
        self.classifier = None
        self.model = None

    def teach(self, count_of_features):
        self._prepare_model(calculate_weights(self.comments, self.answers, self.text_parser), count_of_features)

        self.classifier = GaussianNB()
        self.classifier.fit(self._get_training_set(), self.answers)

    def get_classifier(self):
        return self.classifier

    def get_model(self):
        return self.model

    def _prepare_model(self, weights, count_of_features):
        words_positions = collections.defaultdict(lambda: None)
        words_weights = collections.defaultdict(lambda: None)

        # Needs to retain only maximum weights
        weights = sorted(weights.items(), key=lambda x: abs(x[1]), reverse=True)

        counter = 0
        for data_chunk in weights:
            if counter >= count_of_features:
                break

            words_positions[data_chunk[0]] = counter
            words_weights[data_chunk[0]] = data_chunk[1]
            counter += 1

        self.model = Model(words_positions, words_weights)

    def _get_training_set(self):
        x = []
        for comment in self.comments:
            x.append(get_words_features(comment, self.text_parser, self.model))  # only words used like features by now

        return x