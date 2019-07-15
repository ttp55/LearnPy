#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'WZG'


from io import StringIO, BytesIO

# write to StringIO:
f = StringIO()
f.write('hello')
f.write(' ')
f.write('world!')
print(f.getvalue())


b = BytesIO()
b.write('中文'.encode('utf-8'))
print(b.getvalue())
