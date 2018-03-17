# 偏函数
# python的functool模块提供了很多有用的功能,其中一个就是偏函数(Partial function). 需要注意,这里的偏函数和数学意义上的偏函数不一样.
# 在介绍函数参数的时候,我们讲到,通过设定参数的默认值,可以降低函数调用的难度,而偏函数可以做到这一点,举例如下:
# int() 函数可以把字符串转换为整数,当仅传入字符串,int()函数默认按十进制转换:
result = int('10')
print(result)

# 10进制
result = int('110', base=2)
print('二进制 110 =', result)

# 8进制
result = int('110', 8)
print('八进制 110 = ', result)

print('------------"自定义偏函数"--------------')


# 假设需要转换大量的二进制串,每次都传入int(x,base=2)非常麻烦,于是我们想到,可以定义一个int2()函数,默认把base=2传入
def int2(x, base=2):
    return int(x, base)


print('二进制 110 =', int2("110"))
print('------------"使用functools创建偏函数"--------------')
# functools.partial就是帮助我们创建一个偏函数的,不需要我们定义自己的int2(),可以直接使用下面的代码创建一个新的函数int2
import functools

int2 = functools.partial(int, base=2)
print('二进制 110 =', int2("110"))
