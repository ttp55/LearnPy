#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'WZG'
import multiprocessing
import time


def foo(i):
    time.sleep(0.5)
    print('%s in process ' % i)


if __name__ == '__main__':
    pool = multiprocessing.Pool(5)
    for i in range(5):
        pool.apply(func=foo(i))

    print('end')
    pool.close()
    pool.join()
