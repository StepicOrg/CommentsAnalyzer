# Comments Analyzer 

## Introduction

The purpose of this project is to provide a simple API which could analyze tonality of user comments in real time.

## Example of usage

### Training example

```python
import src.util.file_util as f

from src.util.text.language_model import RUSSIAN
from src.util.text.text_parser import TextParser
from src.preprocessing.training import do_training

comments = []
answers = []

text_parser = TextParser(RUSSIAN)

n_e_classifier, p_n_classifier, model = do_training(comments, answers, text_parser, 1000)

f.dump_model(model, "<path_to_your_folder>\\estimated.txt")
f.dump_classifier(n_e_classifier, "<path_to_your_folder>\\n_e\\model.pkl")
f.dump_classifier(p_n_classifier, "<path_to_your_folder>\\p_n\\model.pkl")
```
The code below train 2 classifiers. The 1st one will separate neutral comments from emotional. The 2nd one will separate positives comments from negatives. After that all classifiers and model dumped in user system.

### Classification usage example

```python
model = f.load_model("<path_to_your_folder>\\estimated.txt")
n_e_classifier = f.load_classifier("<path_to_your_folder>\\n_e\\model.pkl")
p_n_classifier = f.load_classifier("<path_to_your_folder>p_n\\model.pkl")

processor = Processor(n_e_classifier, p_n_classifier, model, text_parser)

comment = ""

tonality = processor.process(comment)
```
The code below illustrates how to use processing logic.

### Note

The *answers* in first example and *tonality* in second could contain only 3 values: -1 - for negative, 0 - for neutral and 1 - for positive comment.
