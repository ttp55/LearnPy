def old(n):
    return n % 2 == 1


print(list(filter(old, range(1, 16))))
