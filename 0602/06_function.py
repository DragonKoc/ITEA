def double (x):
    return 2 * x

print(list(map(double,[1,2,3,4,5])))

print(dict(map(double,'hello')))

def odd(x):
    return x%2

print(list(filter(odd,[1,2,3,4])))

print(dict((('a',1),('b',2))))

import functools

def add(x,y):
    return  x + y


#FOLD
print(functools.reduce(add,[1,2,3])) # (1+2)+3

print('#########  anonim #########')

x = 5
print(list(map(lambda x: 2*x, [1,2,3,4,5])))

f = lambda x:2*x
print(f(2) )
f = lambda :1234
print(f())
print(functools.reduce(lambda x, y : x*y, [12,3,4]))

print([2*x for x in [1,2,3,4,5]])
print([x for x in [1,2,3,4,5] if x%2])

print((1,2)>(2,1)) # False
print((1,2)>(1,1)) # True

print('##### SORT ######')

l = [(2,1),(3,2),(5,4),(1,2)]
l.sort()
print(l)

print(sorted([x for x in [7,8,3,4,5] if x%2]))


l.sort(key=lambda x: x[1])
print(l)

l.sort(key=lambda x: x[0]+ x[1])
print(l)

print('##### SORT one more ######')

ll = [1,'a',2,'b', 2.3]

ll.sort(key=str)
print(ll)

