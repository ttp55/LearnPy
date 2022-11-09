# @Time : 2022/11/9 14:47
# @Author : WZG
# --coding:utf-8--

import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from 机器学习 import knn_fit_class

# 通过测试选择模型

iris = datasets.load_iris()
X = iris.data
y = iris.target


def train_test_split(X, y, test_ratio=0.2, seed=None):
    """将数据 X 和 y 按照test_ratio分割成X_train, X_test, y_train, y_test"""

    assert X.shape[0] == y.shape[0]
    assert 0.0 <= test_ratio <= 1.0

    if seed:
        np.random.seed(seed)

    # 取出X中索引的随机排列
    shuffle_indexes = np.random.permutation(len(X))

    test_size = int(len(X) * test_ratio)

    test_indexes = shuffle_indexes[:test_size]

    train_indexes = shuffle_indexes[test_size:]

    X_train = X[train_indexes]
    y_train = y[train_indexes]

    X_test = X[test_indexes]
    y_test = y[test_indexes]

    return X_train, X_test, y_train, y_test


X_train, X_test, y_train, y_test = train_test_split(X, y)

# 把训练数据集传给knn算法
my_knn_clf = knn_fit_class.KNNClassifier(k=3)
my_knn_clf.fit(X_train, y_train)

# 返回预测数据集
y_predict = my_knn_clf.predict(X_test)

# 将预测数据集与测试数据集进行比对，得到模型预测准确率
print(sum(y_predict == y_test)/len(y_test))
