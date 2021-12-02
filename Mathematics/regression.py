from sklearn.datasets import make_regression
from sklearn.model_selection import train_test_split
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import f_regression 
from sklearn.feature_selection import mutual_info_regression
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

X, y = make_regression(n_samples=1000, n_features=100, n_informative=10, noise=0.1, random_state=42)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=1)

# feature selection
def select_features(X_train, y_train, X_test, strategy=mutual_info_regression):
    """
    strategy: f_regression or mutual_info_regression
    """
    # configure to select all features
    fs = SelectKBest(score_func=f_regression, k='all')
    # learn relationship from training data
    fs.fit(X_train, y_train)
    # transform train input data
    X_train_fs = fs.transform(X_train)
    # transform test input data
    X_test_fs = fs.transform(X_test)

    # what are scores for the features
    fs_score = {}
    for i in range(len(fs.scores_)):
        fs_score.setdefault(i, fs.scores_[i])
        #print('Feature %d: %f' % (i, fs.scores_[i]))
    # plot the scores
    fs_score=pd.Series(fs_score)
    scores = fs_score.sort_values(ascending=True)
    width = np.arange(len(scores))
    ticks = list(scores.index)
    plt.figure(dpi=100, figsize=(40, 12))
    plt.barh(width, scores)
    plt.yticks(width, ticks)
    plt.title(f"{strategy} Scores")
    plt.style.use("seaborn-whitegrid")
    
if __name__ == "__main__": 
    select_features(X_train, y_train, X_test, strategy=f_regression)