def get_features_vector(text, text_parser):
    """
    " Get features vector from text
    """
    #return get_smile_features() + get_punctuation_features() + get_words_features() TODO:
    return []


def get_smile_features():
    # TODO:
    return []


def get_punctuation_features():
    # TODO:
    return []


def get_words_features(text, text_parser, model):
    features = model.get_default_features()

    words = text_parser.correct_all_words(text_parser.get_words(text))
    for word in words:
        index = model.get_word_feature_position(word)
        if index is not None:
            features[index] += model.get_word_feature_weight(word)

    pairs = text_parser.get_words_pairs(words)
    for pair in pairs:
        index = model.get_word_feature_position(pair)
        if index is not None:
            features[index] += model.get_word_feature_weight(pair)

    return features


def get_uno_words():
    # TODO:
    return []


def get_combined_words():
    # TODO:
    return []