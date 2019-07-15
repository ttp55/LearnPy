m = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
]
print(m)
n=[[i[j] for i in m] for j in range(4)]
print(n)
print(m)

del m[0]
print(m)

del m[0][3]
print(m)

#del m[[0][2]:[1][2]]
#print(m)

del m[1][2:4]
print(m)