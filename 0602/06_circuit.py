def f(x):
    def g(y):
        return x*y
    return  g

double = f(2)
print(double(2))

triple = f(3)
print(triple(5))
print(f(2)(5))

print('****************')

def func(t):
    def func2(tt):
        return t + tt
    return func2

lvl1 = func(3)
lvl2 = lvl1(4)

print(str(lvl1)  + " " + str(lvl2))

