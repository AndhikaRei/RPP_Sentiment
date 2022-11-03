# test
from typing import List

import nltk
import re
import numpy as np
import pandas as pd
import itertools
import matplotlib.pyplot as plt
import pickle
import os

from nltk import pos_tag
from nltk.stem import PorterStemmer, SnowballStemmer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from scipy.sparse import hstack
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, precision_recall_fscore_support, confusion_matrix
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from imblearn.over_sampling import RandomOverSampler
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory
from src import rootdir

def normalize_text(string: str, stem: bool=True, sw_elim: bool=True) -> List[str]:
  # filtering, only characters allowed
  filtered = re.sub('[^a-zA-Z]', ' ', string)
  # lower-cased and stemmed using Sastrawi
  stemmed = stemmer.stem(filtered) if stem else filtered.lower()
  # tokenize stemmed string
  tokenized = word_tokenize(stemmed)
  # eliminate stopwords
  res = [word for word in tokenized if word not in stopwords_set] if sw_elim else tokenized
  return res

add_stopwords = set(StopWordRemoverFactory().get_stop_words())

stopwords_set = set(stopwords.words())
stopwords_set = stopwords_set.union(add_stopwords)
stemmer = StemmerFactory().create_stemmer()

df_train = pd.read_csv(os.path.join(rootdir, 'data', 'data.csv'))
df_train.text = df_train.text.apply(normalize_text)
df_train.loc[df_train['label'] == 2, ['label']] = 1

vectorizer_tf = TfidfVectorizer(tokenizer=lambda x: x, preprocessor=lambda x: x)
X_train, y_train = vectorizer_tf.fit_transform(df_train.text), df_train.label