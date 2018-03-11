# tuple的一些操作
# 元数组,不可变
tuple = ('1', '2', '3', '4')
print("tuple =", tuple)
print("tuple[0] =", tuple[0])
tuple = ("1", "2", ["A", "B"])
print("重新赋值后的tuply = ", tuple)
tuple[2][0] = "X"
tuple[2][1] = "Y"
print("改变后的tuply = ", tuple)
