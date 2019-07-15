#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'WZG'

import functools
import time


def log(text='此次'):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('begin %s' % func.__name__)
            start_time = time.perf_counter()
            data = func(*args, **kw)
            stop_time = time.perf_counter()
            dt = stop_time-start_time
            print('end %s' % func.__name__)
            print('%s %s()的执行时间为%f S:' % (text, func.__name__, dt))
            return data
        return wrapper
    return decorator
