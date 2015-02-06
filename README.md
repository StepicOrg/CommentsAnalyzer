<h1>Comments Analyzer</h1>
================
<h1>Introduction:</h1>
<p>The purpose of this project is to provide simple api which could analyze tonality of user comments in real time.</p>
<h1>Example of usage:</h1>

<p>Training example:</p>

import src.util.file_util as f

from src.util.text.language_model import RUSSIAN
from src.util.text.text_parser import TextParser
from src.preprocessing.training import do_training

comments = [] # initialize comments data (strings list)
answers = [] # right classification of each comment

text_parser = TextParser(RUSSIAN)

# train 2 classifiers:
# 1st classifier will separate neutral comments from emotional
# 2nd classifier will separate positive comments from negatives
n_e_classifier, p_n_classifier, model = do_training(comments, answers, text_parser, 1000)

# dump all data
f.dump_model(model, "<path_to_your_folder>\\estimated.txt")
f.dump_classifier(n_e_classifier, "<path_to_your_folder>\\n_e\\model.pkl")
f.dump_classifier(p_n_classifier, "<path_to_your_folder>\\p_n\\model.pkl")
