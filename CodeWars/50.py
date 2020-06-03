# @Time : 2019/10/23 10:32
# @Author : WZG
# --coding:utf-8--


def odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n


def not_divisible(n):
    return lambda x: x % n > 0


class Primes:
    @staticmethod
    def stream():
        yield 2
        it = odd_iter()
        while True:
            n = next(it)
            yield n
            it = filter(not_divisible(n), it)


