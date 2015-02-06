import collections

from src.util.ai.model import Model
from sklearn.externals import joblib

SEPARATOR = '\t'


def load_model(file_name):
    file = open(file_name, mode='r', encoding='utf-8')

    words_positions = collections.defaultdict(lambda: None)
    words_weights = collections.defaultdict(lambda: None)

    full_data = collections.defaultdict(lambda: None)
    for line in file.readlines():
        chunks = line.split(SEPARATOR)
        full_data[chunks[0]] = float(chunks[1])

    weights = sorted(full_data.items(), key=lambda x: abs(x[1]), reverse=True)

    counter = 0
    for data_chunk in weights:
        words_positions[data_chunk[0]] = counter
        words_weights[data_chunk[0]] = data_chunk[1]
        counter += 1

    file.close()

    return Model(words_positions, words_weights)


def dump_model(model, file_name):
    file = open(file_name, mode='w', encoding='utf-8')
    for word, weight in model.words_feature_weights.items():
        file.write(word + SEPARATOR + str(weight) + '\n')

    file.close()


def load_classifier(file_name):
    return joblib.load(file_name)


def dump_classifier(classifier, file_name):
    joblib.dump(classifier, file_name)