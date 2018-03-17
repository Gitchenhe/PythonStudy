# 高阶函数除了可以接受函数作为参数外,还可以把函数作为结果值返回

# 函数作为返回值
def calc_sum(*args):
    ax = 0
    for x in args:
        ax = ax + x
    return ax


# 类似 calc_sum(1,calc_sum(2,calc_sum(3,calc_sum(4))))
result1 = calc_sum(1, 2, 3, 4)
print(result1)


# 但是如果不需要立刻求和,而是在后面的代码中,可以不返回求和的结果,而是范湖求和的函数
def lazy_sum(*args):
    ax = 0

    def calc_sum():
        for x in args:
            ax = ax + x
        return ax

    return calc_sum


result2 = lazy_sum(1, 2, 3, 4)
result3 = lazy_sum(1, 2, 3, 4)
print('lazy 求和', result2, ' result3 == result2', (result3 == result2))


# 闭包
# 注意到返回的函数在其定义内部引用了局部变量args,所以当一个函数返回了一个函数后,其内部变量还没新函数引用,所以闭包用起来简单,实现起来可不容易,
# 另一个需要注意的问题是,返回的函数并没有立即执行,而是直到调用f()才执行
def count1():
    fs = []
    for i in range(1, 4):
        def f():
            return i * i
        fs.append(f)
    return fs;


def count2():
    fs = []
    for i in range(1, 4):
        def g(j):
            def f():
                return j * j

            return f

        fs.append(g(i))
    return fs;


g1, g2, g3 = count1()
f1, f2, f3 = count2()
print("g1=", g1(), 'g2=', g2(), 'g3=', g3())
print("f1=", f1(), 'f2=', f2(), 'f3=', f3())
