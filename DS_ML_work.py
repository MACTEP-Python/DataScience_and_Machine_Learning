import pandas as pd
import numpy as np
import sklearn
from sklearn import tree
import matplotlib.pyplot as plt
import seaborn as sns


train_dogs_cats_df = pd.read_csv('Data/dogs_n_cats.csv')
scores = pd.DataFrame()
for max_depth in range(1,5):
    clf = tree.DecisionTreeClassifier(criterion='entropy', max_depth=max_depth)
    clf.fit(train_dogs_cats_df.iloc[:,:-1], train_dogs_cats_df.iloc[:,-1])
    train_score = clf.score(train_dogs_cats_df.iloc[:,:-1], train_dogs_cats_df.iloc[:,-1])
    temp_score = pd.DataFrame({'max_depth':[max_depth],
                               'train_score':[train_score]})
    scores = pd.concat([scores, temp_score])
