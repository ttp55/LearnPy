from operator import itemgetter
print(sorted([36, 5, -12, 9, -21]))
print(sorted([36, 5, -12, 9, -21],key=abs))
print(sorted(['bob', 'about', 'Zoo', 'Credit']))
print(sorted(['bob', 'about', 'Zoo', 'Credit'],key=str.lower))
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
print(sorted(L))
print(sorted(L,key=itemgetter(0)))
print(sorted(L,key=lambda x:x[1]))
print(sorted(L,key=itemgetter(1),reverse=True))
print(sorted(L,key=lambda m:m[1],reverse=True))

#itemgetter用法
print(itemgetter(0)(L))
print(itemgetter(1)(L))
print(itemgetter(0,1)(L))
