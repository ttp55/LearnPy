i=1
def down(n,x,y):
    if n==1:
        move(n,x,y)
    if n>2:
        down(n-2,x,y)
        move(n,x,y)
        up(n-2,y,x)
    if n>1:
        down(n-1,x,y)
def up(n,p,q):
    if n == 1:
        move(n,p,q)
    if n>1:
        up(n,p,q)
    if n>2:
        down(n-2,p,q)
        move(n,p,q)
        up(n-1,p,q)


def move(n,x,y):
    global i
    print("第%d次操作编号%d从%c到%c\n"%(i,n,x,y))
    i+=1

down(9,'上','下')