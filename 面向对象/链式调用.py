#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'WZG'


class Chain(object):
    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        print(self._path, path)
        return Chain('%s/%s' % (self._path, path))

    def __call__(self, name):
        print(self._path, name)
        return Chain('%s/%s' % (self._path, name))

    def __str__(self):
        return self._path

    __repr__ = __str__


print(Chain().status.user.timeline.list)

print(Chain().users('Tom').repos)
