#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'WZG'

import multiprocessing
import time

my_list = list()


def run_proc(no):
    for i in range(5):
        my_list.append(i)
        #print(no)

        time.sleep(1)
    print(my_list)


def read_data():
    print(my_list)


if __name__ == '__main__':
    pro = multiprocessing.Process(target=run_proc, args=('----2----',))
    proo = multiprocessing.Process(target=read_data)
    pro.start()
    pro.join()
    proo.start()

