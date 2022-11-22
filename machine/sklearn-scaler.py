# @Time : 2022/11/22 9:43
# @Author : WZG
# --coding:utf-8--

import numpy as np
from sklearn import datasets

from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
from sklearn.preprocessing import StandardScaler

iris = datasets.load_iris()

X = iris.data
y = iris.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=666)

standardScaler = StandardScaler()
standardScaler.fit(X_train, y_train)

print(standardScaler.mean_)
print((standardScaler.scale_))
X_train = standardScaler.transform(X_train)

X_test_standard = standardScaler.transform(X_test)

knn_clf = KNeighborsClassifier(n_neighbors=3)
knn_clf.fit(X_train, y_train)

print(knn_clf.score(X_test_standard, y_test))

