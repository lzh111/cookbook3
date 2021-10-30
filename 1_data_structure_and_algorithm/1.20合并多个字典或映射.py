#!/usr/bin/env python
# -*- coding: utf-8 -*-
#   @Time : 2021/6/29 下午8:52
#   @Author : liuzh
#   @desc :
"""
问题：将多个字典或者映射，将它们从逻辑上合并为一个单一的映射后执行某些操作， 比如查找值或者检查某些键是否存在。

解决方案：

"""


a = {'x': 1, 'z': 3 }
b = {'y': 2, 'z': 4 }

from collections import ChainMap
c = ChainMap(a,b)
# 两个字典中执行查找操作（比如先从 a 中找，如果找不到再在 b 中找）
print(c['x']) # Outputs 1 (from a)
print(c['y']) # Outputs 2 (from b)
print(c['z']) # Outputs 3 (from a)

# 一个 ChainMap 接受多个字典并将它们在逻辑上变为一个字典。
# 然后，这些字典并不是真的合并在一起了， ChainMap 类只是在内部创建了一个容纳这些字典的列表 并重新定义了一些常见的字典操作来遍历这个列表。
# 大部分字典操作都是可以正常使用的，比如：
print(len(c))  # 3
print(list(c.keys()))  # ['x', 'y', 'z']
print(list(c.values()))  # [1, 2, 3]


# 如果出现重复键，那么第一次出现的映射值会被返回。 因此，例子程序中的 c['z'] 总是会返回字典 a 中对应的值，而不是 b 中对应的值。
del c['z']
print(c['z'])