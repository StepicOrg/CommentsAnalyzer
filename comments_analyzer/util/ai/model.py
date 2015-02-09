class Model:
    def __init__(self, words_feature_position, words_feature_weights):
        self.words_feature_position = words_feature_position
        self.words_feature_weights = words_feature_weights
        self.features_count = len(words_feature_weights)

    def get_word_feature_position(self, word):
        return self.words_feature_position[word]

    def get_word_feature_weight(self, word):
        return self.words_feature_weights[word]

    def get_default_features(self):
        """
        " Get dict where all features are 0
        """
        return [0 for i in range(self.features_count)]