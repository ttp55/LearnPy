# @Time : 2022/2/17 16:11
# @Author : WZG
# --coding:utf-8--
import random


def on_test():
    i = 0
    while True:
        card_id = random.randint(0, 9 - i)
        i += 1
        print(card_id)
        if card_id == 0:
            return i


if __name__ == '__main__':
    total = 0
    for _ in range(10000):
        total += on_test()
    print(total)
