t = (1,2,3) #1,2,3 tuple
print(type(t))

#распаковка
a,b,c = 'qwe'
print(a,b,c)

a,b,c = 1,2,3
print(a,b,c)

print(a,b)
a,b = b,a
print(a,b)


#кортеж из одного не стоит
tt = 1,


tp = 1,2,3,4,5,6,7

a,b,*c,d = tp

print(a,b,c,d)

t = 1,2,[3,4]
#t[0]=0
t[2][0]=6
print(t)