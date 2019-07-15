dict1 = {}
dict1['one'] = "不懂哎"
dict1[2] = "啥子哦"

tinydict = {'name': 'tom', 'age': 19, 'bir': '1.4'}
print(dict1['one'])
print(dict1[2])
print(tinydict)
print(tinydict.keys())
print(tinydict.values())
print(dict1)
print('tom' in tinydict)
print('name' in tinydict)
print('tom' not in tinydict)
del dict1
d = dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
w = dict([('3sape', 4139), ('guido', 4127), ('jack', 4098)])
print(d)
g = {'sape': 4139, 'guido': 4127, 'jack': 4098}
for k, v in d.items():
    print(k, v)
    # 遍历

for i, j in enumerate(d):
    print(i, j) #'''遍历到索引和对应键'''

for s, x in zip(d,w):
    print(s, x)  #同时遍历多个

for u in reversed(range(20)):
    print(u)  #反向遍历

for a in sorted(d):
    print(a)  #排序遍历
