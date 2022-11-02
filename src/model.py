# test
from typing import List

import re
import numpy as np
import pandas as pd
import itertools
import matplotlib.pyplot as plt

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

df_train = pd.read_csv('../data/data.csv')

add_stopwords = set(StopWordRemoverFactory().get_stop_words())
print('sastrawi stopwords:', len(add_stopwords))

stopwords_set = set(stopwords.words())
print('nltk stopwords:', len(stopwords_set))
stopwords_set = stopwords_set.union(add_stopwords)
print('nltk added stopwords:', len(stopwords_set))

stemmer = StemmerFactory().create_stemmer()
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

df_train.text = df_train.text.apply(normalize_text)
df_train.loc[df_train['label'] == 2, ['label']] = 1

print(df_train.head())

# train, test = train_test_split(df_train, test_size=0.2, random_state=420)

def score_model(true: np.array, pred: np.array, is_svm: bool=True):
  model = 'SVM' if is_svm else 'NaiveBayes'
  print(f'{model} Model Accuracy Score: {accuracy_score(true, pred):.6f}')
  precision, recall, fscore, _ = precision_recall_fscore_support(true, pred, average='macro', zero_division=1)
  print(f'{model} Model Precision Score: {precision:.6f}')
  print(f'{model} Model Recall Score: {recall:.6f}')
  print(f'{model} Model FScore: {fscore:.6f}')
  print(f'{model} Model Confusion Matrix')
  print(confusion_matrix(true, pred))

vectorizer_tf = TfidfVectorizer(tokenizer=lambda x: x, preprocessor=lambda x: x)
X_train, y_train = vectorizer_tf.fit_transform(df_train.text), df_train.label

print(X_train)
print(y_train)

# SVM
svm_model = SVC(C=1.0, kernel='linear', degree=3, gamma='auto')
svm_model.fit(X_train, y_train)

# NAIVE BAYES
nb_model = MultinomialNB()
nb_model.fit(X_train, y_train)

# RBF SVM
svm_model_rbf = SVC(C=1.0, kernel='rbf', degree=3, gamma='auto')
svm_model_rbf.fit(X_train, y_train)

# NB UNIFORM
nb_model_uni = MultinomialNB(fit_prior=False)
nb_model_uni.fit(X_train, y_train)

y_pred_train = svm_model.predict(X_train)
score_model(y_train, y_pred_train)

y_nb_pred_train = nb_model.predict(X_train)
score_model(y_train, y_nb_pred_train, False)

y_pred_train_rbf = svm_model_rbf.predict(X_train)
score_model(y_train, y_pred_train_rbf)

y_nb_pred_train_uni = nb_model_uni.predict(X_train)
score_model(y_train, y_nb_pred_train_uni, False)