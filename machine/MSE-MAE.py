# @Time : 2022/11/22 15:07
# @Author : WZG
# --coding:utf-8--

import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from machine.playML import SimpleLinearRegression, metrics, train_test_split
from math import sqrt


boston = datasets.load_boston()

x = boston.data[:,5]
y = boston.target
x = x[y < 50.0]
y = y[y < 50.0]
plt.scatter(x, y)
print(plt.show())

x_train, x_test, y_train, y_test = train_test_split.train_test_split(x, y, seed=666)

reg = SimpleLinearRegression.SimpleLinearRegression2()
reg.fit(x_train, y_train)


plt.scatter(x_train, y_train)
plt.plot(x_train, reg.predict(x_train), color='r')
print(plt.show())

y_predict = reg.predict(x_test)

mse_test = np.sum((y_predict - y_test)**2) / len(y_test)
print(mse_test)

rmse_test = sqrt(mse_test)
print(rmse_test)

mae_test = np.sum(np.absolute(y_predict - y_test))/len(y_test)
print(mae_test)

from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error
mean_squared_error(y_test, y_predict)
mean_absolute_error(y_test, y_predict)

print(metrics.r2_score(y_test, y_predict))

print(reg.score(x_test, y_test))