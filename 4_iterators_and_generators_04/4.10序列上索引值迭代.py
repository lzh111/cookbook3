data = [(1, 2), (3, 4), (5, 6), (7, 8)]

data_list = [[1, 2, 3], [2, 3, 4], [3, 4, 5]]

# enumerate: 传入一个迭代器，返回一个带索引带迭代器

# Correct!
for n, da in enumerate(data):
    print(type(da))

# Error! 需要注意这一点
# for n, x, y in enumerate(data):
#     print(n, x, y)

for n, [x, y, z] in enumerate(data_list):
    print(n, x, y, z)



a = (1, 2)
print(type(a))
print(type(iter(a)))

