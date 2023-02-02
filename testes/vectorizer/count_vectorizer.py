import pandas as pd
import numpy as np

from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer

import nltk
nltk.download('stopwords')

from nltk.corpus import stopwords

# main

stop = stopwords.words('portuguese')

for stop_word in stop:
    print(stop_word)