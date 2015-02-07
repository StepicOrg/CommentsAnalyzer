from ..util.constants import POSITIVE_TONALITY
from ..util.constants import NEUTRAL_TONALITY
from ..util.constants import NEGATIVE_TONALITY

from ..util.constants import HAS_EMOTION

from ..util.ai.machine_learning import get_words_features


class Processor:
    def __init__(self, has_emotions_classifier, emotions_classifier, model, text_parser):
        self.has_emotions_classifier = has_emotions_classifier
        self.emotions_classifier = emotions_classifier
        self.model = model
        self.text_parser = text_parser

    def process(self, comment):
        x = get_words_features(comment, self.text_parser, self.model)
        if self.has_emotions_classifier.predict(x) == HAS_EMOTION:
            # Do emotions processing
            if self.emotions_classifier.predict(x) == POSITIVE_TONALITY:
                return POSITIVE_TONALITY
            else:
                return NEGATIVE_TONALITY
        else:
            return NEUTRAL_TONALITY