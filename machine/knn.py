# @Time : 2022/11/7 13:40
# @Author : WZG
# --coding:utf-8--

# 近邻算法

import numpy as np
import matplotlib.pyplot as plt
from math import sqrt
from collections import Counter
from machine import knn_classify
from machine import knn_fit_class

raw_data_X = [[3.393533211, 2.331273381],
              [3.110073483, 1.781539638],
              [1.343808831, 3.368360954],
              [3.582294042, 4.679179110],
              [2.280362439, 2.866990263],
              [7.423436942, 4.696522875],
              [5.745051997, 3.533989803],
              [9.172168622, 2.511101045],
              [7.792783481, 3.424088941],
              [7.939820817, 0.791637231]
             ]
raw_data_y = [0, 0, 0, 0, 0, 1, 1, 1, 1, 1]

X_train = np.array(raw_data_X)
Y_train = np.array(raw_data_y)

plt.scatter(X_train[Y_train==0,0], X_train[Y_train==0,1], color='g')
plt.scatter(X_train[Y_train==1,0], X_train[Y_train==1,1], color='r')


x = np.array([8.093607318, 3.365731514]) # 找出x最可能的类型
X_predict = x.reshape(1, -1)

'''
plt.scatter(x[0],x[1], color='b')

# print(plt.show())

distances = [sqrt(np.sum((x_train - x) ** 2)) for x_train in X_train] # 返回离x最近的点


print(distances)

nearest = np.argsort(distances) # 对离x最近的点进行分类

k = 6
topK_y = [Y_train[i] for i in nearest[:k]] #离x最近的6个点的类型

print(topK_y)

votes = Counter(topK_y)# 统计出这6个点的类型，返回值为字典

print(votes.most_common(1)[0][0]) # 找到x最可能的类型

print(knn_classify.KNN_classify(6, X_train, Y_train, x))
'''
knn_clf = knn_fit_class.KNNClassifier(k=6)

print(knn_clf.fit(X_train, Y_train))

y_predict = knn_clf.predict(X_predict)
print(y_predict)

