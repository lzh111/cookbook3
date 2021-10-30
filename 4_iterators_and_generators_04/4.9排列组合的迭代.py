#!/usr/bin/env python
# -*- coding: utf-8 -*-
#   @Time : 2021/10/29 下午2:49
#   @Author : liuzh
#   @desc :

"""
问题： 迭代遍历一个集合中元素的所有可能的排列或组合
"""
from itertools import permutations, combinations_with_replacement, combinations

items = ['a', 'b', 'c']

# 打乱集合中元素的顺序形成的组合
for p in permutations(items):
    print(p)

# 去集合中固定元素形成的集合 (a, b)、(b, a)会保留
for p in permutations(items, 2):
    print(p)

# 可得到输入集合中元素的所有的组合, 长度3(去除重复)
for c in combinations(items, 3):
    print(c)

# 会从指定集合中 取固定长度的组合，可重复取
for c in combinations_with_replacement(items, 3):
    print(c)
