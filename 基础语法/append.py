def f(m):
    n = [1]
    y = 1
    while y < m:
        yield n
        n.append(0)
        print(n)
        n = [n[i-1]+n[i] for i in range(len(n))]
        y += 1
    return


b = f(6)
while True:
    try:
        x = next(b)
        print(x)
    except StopIteration as e:
        print(e.value)
        break
