import enchant

from enchant.utils import trim_suggestions
from enchant.utils import levenshtein


RUSSIAN_DICTIONARY = enchant.Dict('ru_Ru')


def improved_levenshtein_distance(s1, s2):
    # TODO: add word popularity to distance calculation
    return levenshtein(s1, s2)


def correct(word):
    if not RUSSIAN_DICTIONARY.check(word):
        suggestions = RUSSIAN_DICTIONARY.suggest(word)
        if len(suggestions) == 0:   # words could be unknown even for spell checker
            return word

        return trim_suggestions(word, suggestions, 1, improved_levenshtein_distance)[0]

    return word