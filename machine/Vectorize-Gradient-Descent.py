# @Time : 2022/12/1 1:01
# @Author : WZG
# --coding:utf-8--


import numpy as np
from sklearn import datasets
from sklearn.preprocessing import StandardScaler
boston = datasets.load_boston()
X = boston.data
y = boston.target

X = X[y < 50.0]
y = y[y < 50.0]
from machine.playML import train_test_split

X_train, X_test, y_train, y_test = train_test_split.train_test_split(X, y, seed=666)
from machine.playML import LinearRegression

lin_reg1 = LinearRegression.LinearRegression()
lin_reg1.fit_normal(X_train, y_train)
print(lin_reg1.score(X_test, y_test))

lin_reg2 = LinearRegression.LinearRegression()
lin_reg2.fit_gd(X_train, y_train, eta=0.000001, n_iters=1e6)
#print(lin_reg2.score(X_test, y_test))


# 数据归一化 梯度下降
standardScaler = StandardScaler()
standardScaler.fit(X_train)
X_train_standard = standardScaler.transform(X_train)

lin_reg3 = LinearRegression.LinearRegression()
lin_reg3.fit_gd(X_train_standard, y_train)

X_test_standard = standardScaler.transform(X_test)
print(lin_reg3.score(X_test_standard, y_test))