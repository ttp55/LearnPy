#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'WZG'


class Animal(object):
    def eat(self):
        print('Animal can eat')

    def run(self):
        print('Animal can run')


class Dog(Animal):
    def wang(self):
        print('Dog can wang wang wang!')

    def run(self):
        print('Dog can run')


class Cat(Animal):
    def mouse(self):
        print('Cat can catch the mouse!')

    def run(self):
        print('Cat can run')


def run2(animal):
    animal.run()


class Timer(object):
    def run(self):
        print('start...')


dog = Dog()
cat = Cat()

dog.run()
cat.eat()
dog.wang()
cat.mouse()
dog.eat()
run2(Animal())
run2(Dog())
run2(Cat())
print(dir(Dog))
run2(Timer())
