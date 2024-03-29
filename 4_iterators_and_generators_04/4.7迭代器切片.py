#!/usr/bin/env python
# -*- coding: utf-8 -*-
#   @Time : 2021/10/19 上午10:49
#   @Author : liuzh
#   @desc :

"""
问题：由迭代器生成的切片对象，但是标准切片操作并不能做到

迭代器和生成器不能使用标准的切片操作，因为它们的长度事先我们并不知道(并且也没有实现索引)。

函数 islice() 返回一个可以生成指定元素的迭代器，它通过遍历并丢弃直到切片开始索引位置的所有元素。 然后才开始一个个的返回元素，并直到切片结束索引位置。

注：这里要着重强调的一点是 islice() 会消耗掉传入的迭代器中的数据。 必须考虑到迭代器是不可逆的这个事实。 所以如果你需要之后再次访问这个迭代器的话，那你就得先将它里面的数据放入一个列表中。
"""


def generate_data(n):
    data = 0
    while data < n:
        yield data
        data += 1


c = generate_data(20)

# c[10:20] # TypeError: 'generator' object is not subscriptable

cc = list(c)
import itertools

for x in itertools.islice(c, 10, 20):
    print(x)

print(list(c))  # 由于c是islice方法的执行对象，被消耗完了
print(cc)
