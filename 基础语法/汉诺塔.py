i = 1


def hanoi(n, o, t, h):
    if n == 1:
        move(n, o, h)
    else:
        hanoi(n-1, o, h, t)
        move(n, o, h)
        hanoi(n-1, t, o, h)


def move(n, x, y):
    global i
    print("第%d次操作编号%d从%c到%c\n" % (i, n, x, y))
    i += 1


hanoi(9, 'A', 'B', 'C')
