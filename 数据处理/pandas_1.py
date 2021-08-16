# @Time : 2021/8/16 13:58
# @Author : WZG
# --coding:utf-8--

import pandas as pd

a = [1, 2, 3]
b = {1:'一', 2:'二', 3:'三'}

print(pd.Series(a))
print(pd.Series(a)[1])
print(pd.Series(b))
c = [['Google',10],['Runoob',12],['Wiki',13]]
d = {'Site':['Google', 'Runoob', 'Wiki'], 'Age':[10, 12, 13]}
print(pd.DataFrame(c, columns=['Site', 'Age'], dtype=float))
print(pd.DataFrame(d))

nme = ["Google", "Runoob", "Taobao", "Wiki"]
st = ["www.google.com", "www.runoob.com", "www.taobao.com", "www.wikipedia.org"]
ag = [90, 40, 80, 98]

# 字典
dict = {'name': nme, 'site': st, 'age': ag}
pd.DataFrame(dict).to_csv('site.csv')

print(pd.read_csv('site.csv').to_string())

print(pd.read_csv('C:/Users/h/PycharmProjects/LearnPy/数据处理/nba.csv').head())

print(pd.read_csv('C:/Users/h/PycharmProjects/LearnPy/数据处理/nba.csv').info())


print(pd.read_csv('C:/Users/h/PycharmProjects/LearnPy/数据处理/nba.csv').tail())