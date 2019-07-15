# -*- coding: utf-8 -*-
#!/usr/bin/env python3

__author__ = 'WZG'


class Hello(object):
    def hello(self, name='world'):
        print('hello %s' % name)


h = Hello()
print(type(h))
print(type(Hello))
print(h.hello())
