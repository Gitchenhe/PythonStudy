# 装饰器


# 在我们要增强nwo()函数的功能,比如在函数调用前后自动打印日志,但是又不希望修改now()函数的定义,这种代码运行期间动态增加功能的方式,称之为"装饰器
# 本质上,decorator就是一个返回函数的高阶函数.所以,我们要定义一个能打印日志的decorator,可以定义如下
def log(text, name):
    def decorator(fuc):
        def wrapper(*args, **kw):
            print("%s, %s, %s" % (text, name, fuc.__name__))
            func = fuc(*args, **kw)
            print("调用完成")
            return func

        return wrapper

    return decorator


@log(name="显示时间", text="这是text")
def now():
    print('2018-03-11')


f = now
f()


# 解析
# 和两层嵌套decorator相比,3层嵌套的效果是这样的
# now = log('A','B')(now)
# 上面的语句首先执行log('A','B'),返回的decorator函数,在调用返回的函数,参数是now,其返回值最终是wrapper函数.
# 以上两种decorator的定义都没有问题,但是还差最后一步,因为我们讲了函数也是对象,它有__name__等属性,但是你去看经过decorator修饰之后,它们的__name__已经从原来的'now',变为'wrapper'
# 为了便于理解,写如下函数
def func1(val1):
    def func2(val2):
        def func3(val3):
            print(val3)
            return func3

        print(val2)
        return func2

    print(val1)
    return func1


func1('先输出')('再输出')('最后输出')
