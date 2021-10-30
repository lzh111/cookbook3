#!/usr/bin/env python3.7
# _*_ coding: utf-8 _*_
# @Time : 2021/3/20 12:21 
# @Author : 刘子豪 
# @desc : 如果一个可迭代对象的元素个数超过变量个数时，会抛出一个 ValueError 。 那么怎样才能从这个可迭代对象中解压出 N 个元素出来？

"""
问题：
如果一个可迭代对象的元素个数超过变量个数时，会抛出一个 ValueError 。
那么怎样才能从这个可迭代对象中解压出 N 个元素出来？

解决：
Python 的星号表达式可以用来解决这个问题

例子：比如，你在学习一门课程，在学期末的时候， 你想统计下家庭作业的平均成绩，但是排除掉第一个和最后一个分数。
如果只有四个分数，你可能就直接去简单的手动赋值， 但如果有 24 个呢？这时候星号表达式就派上用场了：
"""
from numpy import average

grades = [0, 1, 2, 3, 4, 5, 6, 7, 8, 0]


def drop_last_and_first(grades):
    """
    过滤首尾元素
    :param grades:
    :return:
    """
    first, *middle, last = grades
    return average(middle)


def drop_except_last(grades):
    """
    过滤尾部元素
    :param grades:
    :return:
    """
    *front, last = grades
    return front


print(drop_last_and_first(grades))
print(drop_except_last(grades))


# 星号表达式在迭代元素为可变长元组的序列时
records = [
    ('foo', 1, 2),
    ('bar', 'hello'),
    ('foo', 3, 4),
]  # 带标签的元组序列


def do_foo(x, y):
    print('foo', x, y)


def do_bar(s):
    print('bar', s)


for tag, *args in records:
    if tag == 'foo':
        do_foo(*args)
    elif tag == 'bar':
        do_bar(*args)
