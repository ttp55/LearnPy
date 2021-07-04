# @Time : 2021/4/29 17:52
# @Author : WZG
# --coding:utf-8--
tree = input().split( )
tree = list(map(int, tree))
l = []
tree_right = 1
tree_lift = 0
i = 0
while tree_right <= len(tree) + tree_lift:
        l.append(tree[tree_lift: tree_right])
        tree_lift = tree_right
        tree_right = tree_right * 2 + 1
        i += 1
l = l[::-1]
l = l[1:]
q = []
for i in range(len(l[1:])):
    tr = 1
    tl = 0
    tl1 = 0
    while tr <= len(l[i]):
        try:
            q.append(l[i][tl])
            q.append(l[i][tr])
            q.append(l[i+1][tl1])
            tl += 2
            tr += 2
            tl1 += 1

        except:
            break
q = list(map(str, q))
print(''.join(x+' ' for x in q))


# 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20