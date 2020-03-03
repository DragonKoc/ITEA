def f():
    print('Hello')

f()

def add(x,y):
    return x + y

print(add(5,2))

x=10

def ff():
    print(x)

ff()

#LEGB local enclose global

def f():
    a = 3
    def g():
        def h():
            print(a+1)
        print(a+1)
    g()

a = 10
f()


# def f():
#     print(x)
#     x = 5
#
# f()
xx = 10

def fun():
    global xx
    xx = 7
    return xx

print(fun())
print(xx)

print(help(fun()))


