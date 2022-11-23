# @Time : 2022/11/23 14:08
# @Author : WZG
# --coding:utf-8--

from sklearn import datasets
boston = datasets.load_boston()

X = boston.data
y = boston.target

X = X[y < 50.0]
y = y[y < 50.0]

from machine.playML import LinearRegression, train_test_split

X_train, X_test, y_train, y_test = train_test_split.train_test_split(X, y, seed=666)

reg = LinearRegression.LinearRegression()
reg.fit_normal(X_train, y_train)

print(reg.coef_, reg.intercept_)
print(reg.score(X_test, y_test))
