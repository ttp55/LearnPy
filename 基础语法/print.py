import math
str='Python3'#不可修改

list=['qwer','df','qeqe','1234','abcd']#列表可修改
list1=['ghghg','23432422']
tuple=('qwer','df','qeqe','1234','abcd')#元组与列表的不同点：不可修改
print(str)
print(str[0:-1])
print(str[0])
print(str[2:5])
print(str[2:])
print(str * 2)
print('你好' + ' ' + str)
print('hello\npython')
print(r'hello\nrunoob')
print(str[-2],str[-7])

print(list[0])
print(list + list1)
print(list * 2)
print(list[-2])
print(list[1:4])

for x in range(1,11):
    print(repr(x).rjust(2),repr(x*x).rjust(3),repr(x*x*x).rjust(4),end=' \n')
    #print(repr(x*x*x).rjust(4))

for y in range(1,11):
    print('{0:2d} {1:3d} {2:4d}'.format(y,y*y,y*y*y))#0表示单个y,1表示y*y的格式，2d表示2个宽度的10进制数

print('9'.zfill(9))

print('我在学{name}！，我用{0}'.format('python',name='pyCharm'))

print('{0:.60f}'.format(math.pi))