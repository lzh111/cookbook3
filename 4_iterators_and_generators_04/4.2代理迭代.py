#!/usr/bin/env python3.7
# _*_ coding: utf-8 _*_
# @Time : 2021/3/21 9:53 
# @Author : 刘子豪 
# @desc :

"""
问题：手写迭代对象，怎么实现可迭代

解决：定义__iter__()方法
"""


# python 迭代器协议只是用__iter__()方法 返回一个实现的__next__()的对象
class Node:
    def __init__(self, value):
        self._value = value
        self._children = []

    def __repr__(self):
        return 'Node({!r})'.format(self._value)

    def add_child(self, node):
        self._children.append(node)

    def __iter__(self):
        """将迭代请求传递给self._children"""
        return self._children.__iter__()  # iter(self._children) iter方法底层就是调用__iter__()方法


if __name__ == '__main__':
    root = Node(0)
    child1 = Node(1)
    child2 = Node(2)
    root.add_child(child1)
    root.add_child(child2)

    for ch in root:
        print(ch)
