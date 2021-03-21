#!/usr/bin/env python3.7
# _*_ coding: utf-8 _*_
# @Time : 2021/3/20 22:19 
# @Author : 刘子豪 
# @desc :
"""
问题：怎样实现一个按优先级排序的队列？ 并且在这个队列上面每次 pop 操作总是返回优先级最高的那个元素

解决：heapq 模块实现了一个简单的优先级队列：

"""
import heapq


class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        """添加元素"""
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        """删除元素"""
        return heapq.heappop(self._queue)[-1]


class Item:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return 'Item({!r})'.format(self.name)

q = PriorityQueue()
q.push(Item('f00'), 1)
q.push(Item('bar'), 5)
q.push(Item('spam'), 4)
q.push(Item('grok'), 1)

# 优先级越高 越先被删除，相等看谁先插入，谁先离去
print(q.pop())
