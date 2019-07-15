#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import socketserver


__author__ = 'WZG'


class Animal(object):
    pass


class Mammal(Animal):
    pass


class Bird(Animal):
    pass


class Runnable(object):
    def run(self):
        return print("Running!")


class Flyable(object):
    def fly(self):
        return print("Flying!")


class Carnivorous(object):
    def eatMeat(self):
        return print("eatMeat!")


class Dog(Mammal, Runnable, Carnivorous):
    pass


class Bat(Mammal, Flyable):
    pass


#class MyTCPServer(TCPServer, ForkingMixIn):
#   pass
d = Dog()
print(d.eatMeat(), d.run())

