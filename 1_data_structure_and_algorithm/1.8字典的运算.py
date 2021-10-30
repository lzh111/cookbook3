#!/usr/bin/env python
# -*- coding: utf-8 -*-
#   @Time : 2021/6/29 下午2:08
#   Author : liuzh
#   @desc :


"""
问题：怎样在数据字典中执行一些计算操作（比如求最小值、最大值、排序等等）？


解决:使用 zip() 函数先将键和值反转过来

"""

prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}
# 最小值
min_price = min(zip(prices.values(), prices.keys()))
# 最大值
max_price = max(zip(prices.values(), prices.keys()))
# 排列字典中的数据，按价格排序
prices_sorted = sorted(zip(prices.values(), prices.keys()))

print(min_price)

# 执行这些计算的时候，需要注意的是 zip() 函数创建的是一个只能访问一次的迭代器。 比如，下面的代码就会产生错误：

prices_and_names = zip(prices.values(), prices.keys())
print(min(prices_and_names))  # OK
# print(max(prices_and_names))  # ValueError: max() arg is an empty sequence

#  min() 和 max() 函数中提供 key 函数参数来获取最小值或最大值对应的键的信息
min(prices, key=lambda k: prices[k])  # Returns 'FB'
max(prices, key=lambda k: prices[k])  # Returns 'AAPL'
min_value = prices[min(prices, key=lambda k: prices[k])]


# 当多个实体拥有相同的值的时候，键会决定返回结果。 比如，在执行 min() 和 max() 操作的时候，如果恰巧最小或最大值有重复的，那么拥有最小或最大键的实体会返回：

prices = { 'AAA' : 45.23, 'ZZZ': 45.23 }
min(zip(prices.values(), prices.keys()))  # (45.23, 'AAA')
max(zip(prices.values(), prices.keys()))  # (45.23, 'ZZZ')
