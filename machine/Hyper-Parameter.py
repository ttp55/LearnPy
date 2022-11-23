# @Time : 2022/11/16 14:51
# @Author : WZG
# --coding:utf-8--

import matplotlib
import matplotlib.pyplot as plt
from sklearn import datasets
from machine.playML import metrics, knn_fit_class, train_test_split

digits = datasets.load_digits()

# print(digits.keys())

# print(digits.DESCR)

X = digits.data
y = digits.target
# print(X.shape, y.shape)
some_digit = X[666]

some_digit_image = some_digit.reshape(8, 8)
plt.imshow(some_digit_image, cmap=matplotlib.cm.binary)
# print(plt.show())

X_train, X_test, y_train, y_test = train_test_split.train_test_split(X, y, test_ratio=0.2)

my_knn_clf = knn_fit_class.KNNClassifier(k=3)
my_knn_clf.fit(X_train, y_train)

y_predict = my_knn_clf.predict(X_test)
print(metrics.accuracy_score(y_test, y_predict))
print(my_knn_clf.score(X_test, y_test))



from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=666)

knn_clf = KNeighborsClassifier(n_neighbors=3)
knn_clf.fit(X_train, y_train)

y_predict = knn_clf.predict(X_test)
print(accuracy_score(y_test, y_predict))
