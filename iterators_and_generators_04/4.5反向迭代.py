#!/usr/bin/env python3.7
# _*_ coding: utf-8 _*_
# @Time : 2021/3/21 19:17 
# @Author : 刘子豪 
# @desc :

"""
问题：怎样反方向迭代一个对象

解决：内置reversed()

条件：反向迭代只有当对象的大小可预先知道或实现了__reversed__()方法，如果可迭代对象元素很多的话，
将其预先转换为一个列表需要消耗大量内存
"""

a = [1, 2, 3, 4, 5]
for x in a:
    print(x)