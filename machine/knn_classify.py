# @Time : 2022/11/7 14:49
# @Author : WZG
# --coding:utf-8--

import numpy as np
from math import sqrt
from collections import Counter

# 封装一个class


def KNN_classify(k, X_train, y_train, x):

    assert 1 <= k <= X_train.shape[0], "k must be valid"
    assert X_train.shape[0] == y_train.shape[0]
    assert X_train.shape[1] == x.shape[0]

    distances = [sqrt(np.sum((x_train - x)**2)) for x_train in X_train]
    nearest = np.argsort(distances)

    topK_y = [y_train[i] for i in nearest[:k]]
    votes = Counter(topK_y)

    return votes.most_common(1)[0][0]
