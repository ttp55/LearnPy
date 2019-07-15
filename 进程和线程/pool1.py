#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'WZG'
import multiprocessing
import time, os


def work():
    print("复制中...", os.getpid())
    time.sleep(0.5)


if __name__ == '__main__':
    p = multiprocessing.Pool(6)
    for i in range(7):
        p.apply_async(work())
    p.close()
    p.join()

