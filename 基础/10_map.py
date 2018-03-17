
def f1(x):
    return x*x

def f2(x,y):
    return x+y

result = map(f1,[1,2,3,4,5,6,7])
for x in result:
    print(x)
