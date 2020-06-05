# @Time : 2020/6/4 14:50
# @Author : WZG
# --coding:utf-8--

import pandas as pd
from io import StringIO
from sklearn import linear_model
import matplotlib.pyplot as plt

csv_data = 'square_feet,price\n150,6450\n200,7450\n250,8450\n300,9450\n350,11450\n400,15450\n600,18450\n'

df = pd.read_csv(StringIO(csv_data))
print(df)

# 建立线性回归模型
regr = linear_model.LinearRegression()

#拟合
regr.fit(df['square_feet'].values.reshape(-1, 1), df['price'])

a, b = regr.coef_, regr.intercept_

area = 10000

print(a * area + b)

# print(regr.predict(area))

plt.scatter(df['square_feet'], df['price'], color='blue')

plt.plot(df['square_feet'], regr.predict(df['square_feet'].values.reshape(-1, 1)), color='red', linewidth=4)

plt.show()
