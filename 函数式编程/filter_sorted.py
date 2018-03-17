# python内建的filter函数用于过滤序列

result = filter(lambda x: x < 100, [1, 90, 100, 150])
for item in result:
    print(item)


#
def reversed_cmp(x, y):
    if x > y:
        return -1
    if x < y:
        return 1
    return 0


print("---------演示sorted-------------")
list = [1, 5, 12, 9, 21]
result = sorted(list, reversed_cmp)
for item in result:
    print(item)
