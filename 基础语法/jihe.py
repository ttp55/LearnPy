if __name__ == '__main__':
    print('程序自身在运行')
else:
    print('我来自另一模块')
student={'Tom', 'Jim', 'Mary', 'Tom', 'Jack', 'Rose'}
print(student)

if 'rose' in student :
    print('rose 在集合中')
else :
    print('rose 不在集合中')

a=set('abracadabra')
b=set('alacazam')

print(a)
print(a - b)#差，在a中有，但b中没有
print(a | b)#交，将两个集合合并后去重
print(a & b)#并，同时存在的
print(a ^ b)#a和b不同时存在的元素

a={x for x in a if x not in b}
print(a)