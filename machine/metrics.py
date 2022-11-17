# @Time : 2022/11/16 15:12
# @Author : WZG
# --coding:utf-8--
import numpy as np


def accuracy_score(y_true, y_predict):
    assert y_true.shape == y_predict.shape

    return sum(y_true == y_predict)/len(y_true)
