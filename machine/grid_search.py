# @Time : 2022/11/21 15:50
# @Author : WZG
# --coding:utf-8--

import numpy as np
from sklearn import datasets
from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV


digits = datasets.load_digits()
X = digits.data
y = digits.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=666)

sk_knn_clf = KNeighborsClassifier(n_neighbors=4, weights="uniform")
sk_knn_clf.fit(X_train, y_train)

# 网格搜索，寻找最佳超参数
param_grid = [
    {
        'weights': ['uniform'],
        'n_neighbors': [i for i in range(1, 11)]
    },
    {
        'weights': ['distance'],
        'n_neighbors': [i for i in range(1, 11)],
        'p': [i for i in range(1, 6)]
    }
]


knn_clf = KNeighborsClassifier()

grid_serch = GridSearchCV(knn_clf, param_grid)
grid_serch.fit(X_train, y_train)

print(grid_serch.best_estimator_)
print(grid_serch.best_score_)
print(grid_serch.best_params_)
knn_clf = grid_serch.best_estimator_
print(knn_clf.score(X_test, y_test))

grid_serch = GridSearchCV(knn_clf, param_grid, n_jobs=-1, verbose=3)
print(grid_serch.fit(X_train, y_train))


