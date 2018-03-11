# 参数求和,通常情况下函数是这样定义的
def calc_sum(*args):
    ax = 0
    for x in args:
        ax = ax + x
    return ax


# 但是,如果不需要立即求和,而是在后面的代码中,根据需要再计算怎么办?可以不返回求和的结果,而是返回求和的函数
def lazy_sum(*args):
    def sum():
        ax = 0
        for x in args:
            ax = ax + x
        return ax

    return sum


print("普通求和", calc_sum(1, 2, 3, 4, 5))
print("函数求和", calc_sum(1, 2, 3, 4, 5))


# 闭包
# 每次for循环都会创建一个函数
def count():
    fs = []  # 所有函数的集合
    for i in range(1, 4):
        def f():
            return i * i

        fs.append(f)
    return fs


# f1,f2,f3都指向一个函数
print('--------------- 闭包引用了循环变量,期望值1,4,9 ---------------')
f1, f2, f3 = count()
print('f1()=', f1())
print('f2()=', f2())
print('f3()=', f3())


# 返回结果都是9,原因就是返回的函数变量引用i,但它并非立刻执行,等3个函数都返回时,他们引用的变量都编程了4,因此最终结果是9
# 返回闭包时,请牢记一点:返回函数不要引用任何循环变量,或最后都会发生变化的变量
# 如果一定要引用循环变量怎么办,就是再创建一个函数,用该函数的参数绑定循环变量的当前值,无论循环变量后续如何改变,已经绑定到函数参数的值不变

def count2():
    fs = []
    for i in range(1, 4):
        def f(j):
            def g():
                return j * j

            return g;

        fs.append(f(i))
    return fs


f1, f2, f3 = count2()
print('--------------- 未直接使用循环变量,期望值1,4,9 ---------------')
print('f1()=', f1())
print('f2()=', f2())
print('f3()=', f3())

