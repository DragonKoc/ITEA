for i in 'hello':
    print(i, end='')

print("")

d= {'a':1, 'b':2, 'c':3}

for ii in d:
    print(ii)

print(d.items())

for k,v in d.items():
    print(k,v)

for k in [1,2,3]:
    print(k, end='')

print('')

for ik in range(10):
    print(ik, end='')
print('')

aa=range(10)
cc=range(5,15)
bb = list(range(10))
print(bb)
print(cc)
print(aa)


dic = {'a':1, 'b':2, 'c':3}
for i in dic:
    print(i)
    print(i,dic[i])

for key,value in dic.items():
    print(key,value)


l = [1,2,3,4]
print([2*x for x in l if x%2])

g = (2*x for x in l)
print(list(g))
print(list(g))


