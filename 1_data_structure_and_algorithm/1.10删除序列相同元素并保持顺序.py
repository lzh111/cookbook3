#!/usr/bin/env python
# -*- coding: utf-8 -*-
#   @Time : 2021/6/29 下午2:30
#   @Author : liuzh
#   @desc :

"""
问题：怎样在一个序列上面保持元素顺序的同时消除重复的值？


解决:使用 zip() 函数先将键和值反转过来

"""

# 1. hashable
# 这个方法仅仅在序列中元素为 hashable 的时候才管用
def dedupe(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)


# 如果你想消除元素不可哈希（比如 dict 类型）的序列中重复元素的话，你需要将上述代码稍微改变一下
def dedupe(items, key=None):
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)

#>>> a = [ {'x':1, 'y':2}, {'x':1, 'y':3}, {'x':1, 'y':2}, {'x':2, 'y':4}]
# >>> list(dedupe(a, key=lambda d: (d['x'],d['y'])))
# [{'x': 1, 'y': 2}, {'x': 1, 'y': 3}, {'x': 2, 'y': 4}]
# >>> list(dedupe(a, key=lambda d: d['x']))
# [{'x': 1, 'y': 2}, {'x': 2, 'y': 4}]
# >>>