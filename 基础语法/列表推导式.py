from 基础语法 import jihe

n=list(range(1,16,4))
m=list(range(2,18,3))
q=[i*j for i in n if i<12 for j in m if j<17]
print(q)

print(jihe.student)