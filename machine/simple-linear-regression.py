# @Time : 2022/11/22 13:45
# @Author : WZG
# --coding:utf-8--

import numpy as np
import matplotlib.pyplot as plt
from machine import SimpleLinearRegression

x = np.array([1., 2., 3., 4., 5.])
y = np.array([1., 3., 2., 3., 5.])
plt.scatter(x, y)
plt.axis([0, 6, 0, 6])


x_mean = np.mean(x)
y_mean = np.mean(y)

num = 0.0
d = 0.0
for x_i, y_i in zip(x, y):
    num += (x_i - x_mean) * (y_i - y_mean)
    d += (x_i - x_mean) ** 2
a = num/d
b = y_mean - a * x_mean
y_hat = a * x + b
plt.scatter(x, y)
plt.plot(x, y_hat, color='r')
plt.axis([0, 6, 0, 6])
print(plt.show())
x_predict = 6
y_predict = a * x_predict + b
print(y_predict)

reg1 = SimpleLinearRegression.SimpleLinearRegression1()
reg1.fit(x, y)
print(reg1.predict(np.array([x_predict])))
print(reg1.a_, reg1.b_)
