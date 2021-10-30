#!/usr/bin/env python3.7
# _*_ coding: utf-8 _*_
# @Time : 2021/3/21 10:01 
# @Author : 刘子豪 
# @desc :

"""
问题：实现一个自定义迭代模式，跟普通的内置函数比如 range() , reversed() 不一样

解决：如果你想实现一种新的迭代模式，使用一个生成器函数来定义它

"""


# 一个函数中有yield 可以将其转换成生成器，生成器只能用于迭代操作
def frange(start, stop, increment):
    """生成某个范围内的浮点数"""
    x = start
    while x < stop:
        yield x
        x += increment


for i in frange(0, 4, 0.5):
    print(i)


def countdown(n):
    while n > 0:
        yield n
        n -= 1
    print('Done')


c = countdown(3)
print(next(c))
print(next(c))
print(next(c))
print(next(c))
