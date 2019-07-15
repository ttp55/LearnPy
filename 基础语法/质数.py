n = 0


for i in range(2, 10000):
    for j in range(2, i):
        if i % j == 0:
            print("%d等于%d*%d" % (i, j, i//j))
            break
    else:
        n = n+1
        print("%d是第%d个质数"%(i,n))
