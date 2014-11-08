"""
    Initially this spell checker gets from
    "https://github.com/mattalcock/blog/blob/master/2012/12/5/python-spell-checker.rst",
    but it needs to be improved:
    TODO: needs to check changes weight to select the most relevant word;
"""

import collections


def load_known_words(file_name):
    """
    " Use this function if you already prepare
    " known_words_model to load.
    """
    model = collections.defaultdict(lambda: 1)

    file = open(file_name, "r", encoding='utf-8')
    for line in file.readlines():
        data = line.split('\t')
        model[data[0]] = int(data[1])

    return model


def train(features):
    """
    " Use this function if you needs to prepare
    " your model on known words set.
    """
    model = collections.defaultdict(lambda: 1)
    for f in features:
        model[f] += 1
    return model


alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'


def edits(word):
    s = [(word[:i], word[i:]) for i in range(len(word) + 1)]
    deletes    = [a + b[1:] for a, b in s if b]
    transposes = [a + b[1] + b[0] + b[2:] for a, b in s if len(b)>1]
    replaces   = [a + c + b[1:] for a, b in s for c in alphabet if b]
    inserts    = [a + c + b     for a, b in s for c in alphabet]
    return set(deletes + transposes + replaces + inserts)


def known_edits(word, known_words):
    return set(e2 for e1 in edits(word) for e2 in edits(e1) if e2 in known_words)


def known(words, known_words):
    return set(w for w in words if w in known_words)


def correct(word, known_words):
    candidates = known([word], known_words) \
                 or known(edits(word), known_words) \
                 or known_edits(word, known_words) \
                 or [word]

    return max(candidates, key=known_words.get)