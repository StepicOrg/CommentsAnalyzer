<h1>Comments Analyzer</h1>
================
<h1>Introduction:</h1>
<p>The purpose of this project is to provide simple api which could analyze tonality of user comments in real time.</p>
<h1>Example of usage:</h1>

<h3>Training example:</h3>

<h6>import src.util.file_util as f</h6>

<h6>from src.util.text.language_model import RUSSIAN</h6>
<h6>from src.util.text.text_parser import TextParser</h6>
<h6>from src.preprocessing.training import do_training</h6>

<h6>comments = []</h6>  initialize comments data (strings list)
<h6>answers = []</h6>  right classification of each comment

<h6>text_parser = TextParser(RUSSIAN)</h6>

train 2 classifiers:
1st classifier will separate neutral comments from emotional
2nd classifier will separate positive comments from negatives
<h6>n_e_classifier, p_n_classifier, model = do_training(comments, answers, text_parser, 1000)</h6>

dump all data
<h6>f.dump_model(model, "<path_to_your_folder>\\estimated.txt")</h6>
<h6>f.dump_classifier(n_e_classifier, "<path_to_your_folder>\\n_e\\model.pkl")</h6>
<h6>f.dump_classifier(p_n_classifier, "<path_to_your_folder>\\p_n\\model.pkl")</h6>
