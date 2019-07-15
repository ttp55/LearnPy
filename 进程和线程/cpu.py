# @Time : 2019/5/5 15:33
# @Author : WZG
# --coding:utf-8--

# 占满一个CPU
import threading, multiprocessing


def loop():
    x = 0
    while True:
        x = x ^ 1


for i in range(multiprocessing.cpu_count()):
    t = threading.Thread(target=loop)
    t.start()

