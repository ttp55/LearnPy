#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'WZG'


class Screen(object):

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, width):
        self._width = width

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, height):
        self._height = height

    @property
    def resolution(self):
        return self._width * self._height


s = Screen()
s.height = 180
s.width = 150
print(s.height, s.width, s.resolution)
if s.resolution == 27000:
    print('测试通过~')
else:
    print('测试失败！')