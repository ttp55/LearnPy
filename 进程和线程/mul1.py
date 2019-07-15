#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'WZG'
import multiprocessing
import time


def work():
    for i in range(10):
        print('working...')
        time.sleep(0.2)


if __name__ == '__main__':
    pro = multiprocessing.Process(target=work)
    pro.start()
    #让主进程等待1秒
    time.sleep(1.5)
    print('main is done ...')
    #让子进程直接销毁，表示终止执行
    pro.terminate()
    #主进程会等待所有子进程执行完成后程序再退出
