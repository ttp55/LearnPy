import sys

L = list(range(100))

it = iter(L)
print(next(it))
print(next(it))

while True:
    try:
        print(next(it))
    except StopIteration:
        sys.exit()
