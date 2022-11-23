# @Time : 2022/11/7 15:16
# @Author : WZG
# --coding:utf-8--


import numpy as np
from math import sqrt
from collections import Counter
from machine.playML import metrics


class KNNClassifier:

    def __init__(self, k):
        """初始化KNN分类器"""
        assert k>=1
        self.k = k
        self._X_train = None
        self._y_train = None

    def fit(self, X_train, y_train):
        """根据训练数据集X_train和y_train训练KNN分类器"""
        assert X_train.shape[0] == y_train.shape[0]
        assert self.k <= X_train.shape[0]

        self._X_train = X_train
        self._y_train = y_train

        return self

    def predict(self, X_predict):
        """给定待预测数据集X_predict，返回表示X_predict的结果向量"""

        assert self._X_train is not None and self._y_train is not None
        assert X_predict.shape[1] == self._X_train.shape[1]

        y_predict = [self._predict(x) for x in X_predict]
        return np.array(y_predict)

    def _predict(self, x):
        """给定单个待测数据x， 返回x的预测结果值"""

        assert x.shape[0] == self._X_train.shape[1]

        distances = [sqrt(np.sum((x_train - x) ** 2)) for x_train in self._X_train]
        nearest = np.argsort(distances)

        topK_y = [self._y_train[i] for i in nearest[:self.k]]
        votes = Counter(topK_y)

        return votes.most_common(1)[0][0]

    def score(self, X_test, y_test):
        """根据X_test和 y_test预测模型准确度"""

        y_predict = self.predict(X_test)
        return metrics.accuracy_score(y_test, y_predict)

    def __repr__(self):
        return "KNN(k=%d)" % self.k
