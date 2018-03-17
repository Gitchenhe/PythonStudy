# 将abs函数作为变量,传给形参
def add(x,y,f):
    return f(x) + f(y)

print(add(-1,1,abs))