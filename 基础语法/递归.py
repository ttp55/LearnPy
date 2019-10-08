def jieC(n):
    if n==1:
        return 1
    print(n)
    return (n*jieC(n-1))

print(jieC(10))