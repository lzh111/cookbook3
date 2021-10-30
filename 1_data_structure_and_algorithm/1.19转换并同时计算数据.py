#!/usr/bin/env python
# -*- coding: utf-8 -*-
#   @Time : 2021/6/29 下午8:37
#   @Author : liuzh
#   @desc :

"""
问题：转换或者过滤数据

解决方案：结合数据计算与转换就是使用一个生成器表达式参数

"""

nums = [1, 2, 3, 4, 5]
s = sum(x * x for x in nums)

# Determine if any .py files exist in a directory
import os
files = os.listdir('')
if any(name.endswith('.py') for name in files):
    print('There be python!')
else:
    print('Sorry, no python.')
# Output a tuple as CSV
s = ('ACME', 50, 123.45)
print(','.join(str(x) for x in s))
# Data reduction across fields of a data structure
portfolio = [
    {'name':'GOOG', 'shares': 50},
    {'name':'YHOO', 'shares': 75},
    {'name':'AOL', 'shares': 20},
    {'name':'SCOX', 'shares': 65}
]
min_shares = min(s['shares'] for s in portfolio)


s = sum((x * x for x in nums)) # 显式的传递一个生成器表达式对象
s = sum(x * x for x in nums) # 更加优雅的实现方式，省略了括号


# 这种方式同样可以达到想要的效果，但是它会多一个步骤，先创建一个额外的列表。
# 对于小型列表可能没什么关系，但是如果元素数量非常大的时候，
# 它会创建一个巨大的仅仅被使用一次就被丢弃的临时数据结构。
# 而生成器方案会以迭代的方式转换数据，因此更省内存。
nums = [1, 2, 3, 4, 5]
s = sum([x * x for x in nums])


# 在使用一些聚集函数比如 min() 和 max() 的时候你可能更加倾向于使用生成器版本，
# 它们接受的一个 key 关键字参数或许对你很有帮助。
# Original: Returns 20
min_shares = min(s['shares'] for s in portfolio)
# Alternative: Returns {'name': 'AOL', 'shares': 20}
min_shares = min(portfolio, key=lambda s: s['shares'])