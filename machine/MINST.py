# @Time : 2022/12/2 14:56
# @Author : WZG
# --coding:utf-8--

import numpy as np

# from sklearn.datasets import fetch_mldata
# mnist = fetch_mldata('MNIST original')
# 在最新版的 sklearn 中，fetch_mldata 被弃用，改为使用 fetch_openml 获得 MNIST 数据集
# 具体见如下代码，后续代码无需改变

from sklearn.datasets import fetch_openml

mnist = fetch_openml('mnist_784')

print(mnist)

X, y = mnist['data'], mnist['target']
X_train = np.array(X[:60000], dtype=float)
y_train = np.array(y[:60000], dtype=float)
X_test = np.array(X[60000:], dtype=float)
y_test = np.array(y[60000:], dtype=float)

from sklearn.neighbors import KNeighborsClassifier

knn_clf = KNeighborsClassifier()
knn_clf.fit(X_train, y_train)

print(knn_clf.score(X_test, y_test))

from sklearn.decomposition import PCA
pca = PCA(0.90)
pca.fit(X_train)
X_train_reduction = pca.transform(X_train)
X_test_reduction = pca.transform(X_test)

knn_clf = KNeighborsClassifier()
knn_clf.fit(X_train_reduction, y_train)

print(knn_clf.score(X_test_reduction, y_test))
