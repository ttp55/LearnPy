# @Time : 2019/5/21 9:04
# @Author : WZG
# --coding:utf-8--


x = [18, 18, 19, 19, 24, 23, 22, 22, 21, 20, 19, 22, 23, 24, 24]
y = [25, 28, 30, 29, 28, 27, 27, 25, 26, 25, 26, 27, 24]
z = [31, 33, 32, 32, 32, 34, 34, 35, 36, 35, 36, 37, 30, 30]

lst = x + y + z

print('平均月龄{:.2f}'.format(sum(lst)/len(lst)))
print('最大月龄：%d' % max(lst))
print('最小月龄：%d' % min(lst))
print(f'月龄为30的有{lst.count(30)}个')
s1 = 0
s2 = 0
for x in range(1, 100, 2):
    s1 += x
for i in range(2, 100, 2):
    s2 += i

print(s1 - s2 + 88)
print(77 % 88)

