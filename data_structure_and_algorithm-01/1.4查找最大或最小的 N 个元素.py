#!/usr/bin/env python3.7
# _*_ coding: utf-8 _*_
# @Time : 2021/3/20 16:46 
# @Author : 刘子豪 
# @desc :
"""
问题：怎样从一个集合中获得最大或者最小的 N 个元素列表？

解决方案：heapq 模块有两个函数：nlargest() 和 nsmallest()
你想在一个集合中查找最小或最大的 N 个元素，并且 N 小于集合元素数量，那么这些函数提供了很好的性能。
因为在底层实现里面，首先会先将集合数据进行堆排序后放入一个列表中：
"""

import heapq

nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
print(heapq.nlargest(3, nums))  # 最大三个元素
print(heapq.nsmallest(3, nums))  # 最小三个元素

# 可接收关键字参数
portfolio = [
    {'name': 'IBM', 'shares': 100, 'price': 91.1},
    {'name': 'AAPL', 'shares': 50, 'price': 543.22},
    {'name': 'FB', 'shares': 200, 'price': 21.09},
    {'name': 'HPQ', 'shares': 35, 'price': 31.75},
    {'name': 'YHOO', 'shares': 45, 'price': 16.35},
    {'name': 'ACME', 'shares': 75, 'price': 115.65}
]
cheap = heapq.nsmallest(3, portfolio, key=lambda s: s['price'])
expensive = heapq.nlargest(3, portfolio, key=lambda s: s['price'])
print(cheap)
print(expensive)


nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
import heapq
heap = list(nums)
heapq.heapify(heap)
print(heap)
# 堆的数据结构最重要的特征是heap[0]永远是最小的的元素，剩余元素可以用heapq.heappop()
# 该方法会将第一个元素弹出，将下一个最小的元素取代被弹元素。时间复杂度logN
# sorted(items)[:N]