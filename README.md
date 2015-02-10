<h1>Comments Analyzer</h1>
================
<h1>Introduction:</h1>
<p>The purpose of this project is to provide simple api which could analyze tonality of user comments in real time.</p>
<h1>Example of usage:</h1>

<h3>Training example:</h3>

```python
import comments_analyzer.common.file_util as f

from comments_analyzer.text.language_model import RUSSIAN
from comments_analyzer.text.text_parser import TextParser
from comments_analyzer.training import do_training

comments = []
answers = []

text_parser = TextParser(RUSSIAN)

n_e_classifier, p_n_classifier, model = do_training(comments, answers, text_parser, 1000)

f.dump_model(model, "<path_to_your_folder>\\estimated.txt")
f.dump_classifier(n_e_classifier, "<path_to_your_folder>\\n_e\\model.pkl")
f.dump_classifier(p_n_classifier, "<path_to_your_folder>\\p_n\\model.pkl")
```
The code below train 2 classifiers. The 1st one will separate neutral comments from emotional. The 2nd one will separate positives comments from negatives. After that all classifiers and model dumped in user system.

<h3>Classification usage example:</h3>
```python
model = f.load_model("<path_to_your_folder>\\estimated.txt")
n_e_classifier = f.load_classifier("<path_to_your_folder>\\n_e\\model.pkl")
p_n_classifier = f.load_classifier("<path_to_your_folder>p_n\\model.pkl")

processor = Processor(n_e_classifier, p_n_classifier, model, text_parser)

comment = ""

tonality = processor.process(comment)
```
The code below illustrates how to use processing logic.

<h3>Note:</h3>
The <i>answers</i> in first example and <i>tonality</i> in second could contain only 3 values: -1 - for negarive, 0 - for neutral and 1 - for positive comment.
