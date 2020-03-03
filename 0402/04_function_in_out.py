def f(x,y=2):
    return x*y

print(f(2))


def ff(a=1,b=2,c=4):
    return a+b+c

print(ff())

# def fff(2,[1,2,3]):
#
# print(fff(2))


print(max(1,2,3))

def df(*args, **kwargs):
    print(args,kwargs)

print(df(1,2,3,a=3,b=4))

def sum_(*items):
    a=0
    for item in items:
        a += item
    return a

print(sum_(1,2,3,4))




t = 1,2,3
print(f(t))
#print(f_(*t))