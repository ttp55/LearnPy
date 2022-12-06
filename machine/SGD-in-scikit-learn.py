# @Time : 2022/12/1 1:39
# @Author : WZG
# --coding:utf-8--


import numpy as np
import matplotlib.pyplot as plt
m = 100000

x = np.random.normal(size=m)
X = x.reshape(-1,1)
y = 4.*x + 3. + np.random.normal(0, 3, size=m)
from machine.playML import LinearRegression
lin_reg = LinearRegression.LinearRegression()
lin_reg.fit_bgd(X, y)
print(lin_reg.intercept_, lin_reg.coef_)

lin_reg = LinearRegression.LinearRegression()
lin_reg.fit_sgd(X, y, n_iters=2)
print(lin_reg.intercept_, lin_reg.coef_)

from sklearn.linear_model import SGDRegressor
from sklearn import datasets

boston = datasets.load_boston()
X = boston.data
y = boston.target

X = X[y < 50.0]
y = y[y < 50.0]
from machine.playML import train_test_split

X_train, X_test, y_train, y_test = train_test_split.train_test_split(X, y, seed=666)
from sklearn.preprocessing import StandardScaler

standardScaler = StandardScaler()
standardScaler.fit(X_train)
X_train_standard = standardScaler.transform(X_train)
X_test_standard = standardScaler.transform(X_test)
sgd_reg = SGDRegressor()
sgd_reg.fit(X_train_standard, y_train)
print(sgd_reg.score(X_test_standard, y_test))