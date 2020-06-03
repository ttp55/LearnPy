# @Time : 2019/12/5 10:58
# @Author : WZG
# --coding:utf-8--

from collections import Counter
import re
a = 'kjalfj;ldsjafl;hdsllfdhg;lahfbl;hl;ahlf;h'
r = Counter(a)
print(type(r))
print(dict(r))
print(r['p']) # dict /访问不存在的key会报错 counter不会报错，它返回0

b = 'not 404 found 张三 99 深圳'
l = re.findall('\d+|[a-zA-Z]+', b)
l1 = list(b.split(' '))
for i in l:
    if i in l1:
        l1.remove(i)
print(l1)

m = list(range(1, 11))
nl = list(filter(lambda y: y % 2 == 1, m))
print(nl)
nn = [i for i in m if i % 2 == 1]
print(nn)

l1 = [1, 5, 7, 9]
l2 = [2, 6, 2, 8]
print(sorted(l1+l2))

oo = re.search('\d+', b)
print(oo.group())
pp = re.match('[a-zA-Z]', b)
print(pp)

print([x for i in [[1, 2], [3, 4], [5, 6]] for x in i])

print('abc'.join(['d', 'e', 'f']))
print('abc'.join('def'))
print([1, 2, 3] + [4, 5, 6])

print(re.sub('\d+', '100', '张明 98分'))


l = ['a', 'b', 'c', 'd', 'e', 'f']
print(list(zip(l[:-1], l[1:])))

nums = ['flower', 'flow', 'flight']
for i in zip(*nums):
    print(i)

foo =  [-5,8,0,4,9,-4,-20,-2,8,2,-4]
print(sorted(foo))


x = 0b10100
print(type(x))
print(x)