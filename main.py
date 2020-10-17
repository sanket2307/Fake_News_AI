from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
from sklearn import metrics
from sklearn.metrics import confusion_matrix
import seaborn as sns
import numpy as np
import pandas as pd

import os
import re
import nltk

train = pd.read_csv('train.csv')
test = pd.read_csv('test.csv')
