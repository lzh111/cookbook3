# -*- coding: utf-8 -*-

# 在多个对象执行相同的操作

# 传统上
from itertools import chain

active_items = set()
inactive_items = set()
for item in active_items:
    pass
for item in inactive_items:
    pass

# 改进后
for item in chain(active_items, inactive_items):
    pass

"""
如果输入序列非常大的时候会很省内存，a + b 操作会创建一个全新的序列并要求a和b的类型一致，chian() 不会有这一步。
"""
