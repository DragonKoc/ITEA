i = 1000

# while i>100:
#     print(i, end=' ')
#     i /=2

for j in 'hello world':
    if j=='h':
        continue
    print(j * 2, end ='')
else:
    print('end with break')
a=5


lis = [1,22,333]
print(lis)
lis.append(56)
print(lis)
lis.extend([45,34])
print(lis)

a = [a + b for a in 'kostya' if a!='s' for b in 'grebenyuk' if b!= 'u']
print(a)
print(a.count('yy'))
print(a.index('yy'))
print(a)
try:
    print(a.index(2))
except ValueError:
    print('oshubochka')

l = []

for i in '12345':
    l.extend(i)
print(l)

ii=0
while ii < 5:
    print(l[ii])
    ii+=1


tup = (1,2,3,[4,5])
print(tup)
tup[3][0] = 'a'
print(tup)

d = {'name' : 'koc', 'surname' : 'grebenyuk'}
dd = dict(d)
print(d)
dd['name'] = 5
print(dd)

ddd = {a : a ** 2 for a in range(7)}
print(ddd)

person = {'name' : {'surname' : 'Grebenyuk', 'name': 'Koc'}, 'adress' : ['Kiev', 'Antonovicha', '11'], 'phone' : {'home_phone': '55-55-55', 'work_phone':'33-33-33'}}

print(person['name']['name'])

print(person['adress'][2])
print(person.values())
print(person.keys())


def func (ak):
    return ak*2

print(func(2))

a,b,c = input().split (",")
print(a,b,c)