#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'WZG'

from multiprocessing import Process

import os

i = 'test'


def run_proc(name):
    print('Run child process %s (%s)' % (name, os.getpid()))


if __name__ == '__main__':
    print('Parent process %s' % os.getpid())
    p = Process(target=run_proc('tes'))
    print('Child process will start')
    p.start()
    p.join()
    print('Child process end.')
