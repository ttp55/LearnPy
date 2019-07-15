#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'WZG'

from multiprocessing import Process

import os


print('Process(%s) start...' % os.getpid())

pid = os.fork()
if pid == 0:
    print('I am chile proces (%s) and my parent is %s' % (os.getpid(), os.getpid()))
else:
    print('I (%s) just created a child process (%s)' % (os.getpid(), pid))

