#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'WZG'
import multiprocessing
import time


def write_que(q):
    for i in range(10):
        if q.full():
            print('队列满了。。。')
            break
        q.put(i)
        time.sleep(0.2)
        print(i)


def read_que(q):
    while True:
        if q.qsize() == 0:
            print('队列空了。。。')
            break
        value = q.get()
        print(value)


if __name__ == '__main__':
    q = multiprocessing.Queue(5)

    write_q = multiprocessing.Process(target=write_que(q))
    read_q = multiprocessing.Process(target=read_que(q))

    write_q.start()
    write_q.join()
    read_q.start()
