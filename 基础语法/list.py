list = [1,2,3,4]
list1 = [5,6,7,8]

list.append(5)
print(list)#在列表最后插入

list.extend(list1)
print(list)#拼凑

list.insert(3,3.5)
print(list)#向指定位置插入元素

list.remove(2)
print(list)#删除索引位置元素

list. pop()
print(list)#把第索引位元素移除并返回

#list.clear()
#print(list)#清空列表

list.insert(1,3)
print(list)

print(list.index(3))#返回第一个元素的索引

print(list.count(3))#返回一个元素在列表中出现的次数

list.reverse()#将目标列表倒序排列
print(list)

print(list.copy())#返回一个列表的浅复制

#可以用append和pop方法将列表做为一个栈使用，如：
list.append(8)
list.pop()