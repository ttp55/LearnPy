#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'WZG'
from multiprocessing import Pool
import os, time, random


def fun(i):
    time.sleep(0.5)
    print('in process...', i)


def mul(func, n):
    poo = Pool(processes=n)
    for i in range(n):
        poo.apply_async(func, (i,))
    poo.close()
    poo.join()


if __name__ == '__main__':
    mul(fun, 4)
