#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'WZG'
import multiprocessing


if __name__ == '__main__':
    queue = multiprocessing.Queue(3)
    queue.put(1)
    queue.put('hello')
    queue.put([3, 5])
    #queue.put(4)

    if queue.qsize() == 0:
        print('queue is null')
    else:
        print('queue is not null')

print(queue.full())
size = queue.qsize()
print(size)

value = queue.get()
print(value)

size = queue.qsize()
print(size)

value = queue.get()
print(value)

value = queue.get()
print(value)

size = queue.qsize()
print(size)

queue.put([6, 9])

size = queue.qsize()
print(size)
value = queue.get()
print(value)
