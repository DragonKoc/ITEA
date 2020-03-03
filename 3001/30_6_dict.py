#dictionary

d = {} #hash table
print(type(d))

d['a']=1
print(d)
d[3]='b'
print(d)
print(d['a'])

print('a' in d)

d= {'a':1, 'b':2, 'c':3}
print(d['a'])

print({1,2}|{3,4})
print({1,2}&{2,4})
print({1,2}-{2,4})
print({1,2}^{2,4})

s = [1,2,3,1]
print(set(s))
#s.add(4)
print(s)

print(type(None))