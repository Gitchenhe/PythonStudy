# python 内建了map()和reduce()函数
# map()接收连个参数,一个是函数,一个是序列,map()将传入的函数依次作用到序列的每个元素上,并把结果作为新的list返回
from functools import reduce


def add(x, y):
    return x + y


result = map(add, [1, 2, 3], [1, 2, 3])

print("-----------演示map---------------")
for item in result:
    print(item)

print("-----------演示reduce---------------")
result = reduce(add, [1, 2, 3])
print(result)

# list转字符串
print("[1, 2, 3, 4] 转字符串")


def toString(x, y):
    return str(x) + str(y)


result = reduce(toString, [1, 2, 3, 4])
print(result)

print("字符串['1','2','3','4','5']转int")


def toInt(x, y):
    return x + y


result = reduce(toInt, ['1', '2', '3', '4', '5'])
print(result)

print("使用lambda替代上述方法")
result = reduce(lambda x, y: x + y, ['1', '2', '3', '4', '5'])
print(result)
