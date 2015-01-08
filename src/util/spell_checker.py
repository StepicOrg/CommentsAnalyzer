import enchant


RUSSIAN_DICTIONARY = enchant.Dict('ru_Ru')


def correct(word, known_words):
    # TODO: improve best word selection
    if not RUSSIAN_DICTIONARY.check(word):
        suggestions = RUSSIAN_DICTIONARY.suggest(word)
        return suggestions[0] if len(suggestions) > 0 else word     # words could be unknown even for spell checker

    return word