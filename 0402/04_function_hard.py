def f(x):
    return 2*x

double = f

print(double(2))

##################
print('######')

def execute (f,x):
    return f(x)

print(execute(double,5))

##################
print('######')

def f():
    def g(x):
        return 3*x
    return g

print(double(2))
print(f()(2))

##################
print('######map')

map(double, [1,2,3,4])
print(list(map(double, [1,2,3,4])))

##################
print('######')

def odd(x):
    return x%2

print(odd(2))
print(odd(3))
print(list(filter(odd,[1,2,3,4])))

##################
print('######')

import functools
def add(x,y):
    return x + y

res1 = functools.reduce(add,[1,2,3,4])
print(res1)


