l = [1,2,6,'dfds',[2,5]]

print (l)

print(len(l))
print(l[0])
l[0]=123
print(l)
l[1:3]=[1,2,3,4,5]
print(l)

l1=[1,2,3]
l2=l1
print(l1,l2)
l1[0]=0
print(l1,l2) #l2 link to l1


l2 = l1[:] #python2
l2 = l1.copy()
l1[1]=0
print(l1,l2)

###
print('#####')
l1 = [1,2,[3,4]]
l2 = l1.copy()
print(l1,l2)
l1[2][0]='a'
print(l1,l2)

import copy
l2 = copy.deepcopy(l1)#full copy

print('#####METHOD######')

l=[1,2,3,4,5]
l.append(1) #вставка в начало
print(l)
print(l.count(1))
l.extend([1,2,3]) #вставка в конец
print(l)
l.append([1,2,3])
print(l)
print(l.index(2,2))
print(l.count(2))
#print(l.index(2,8))

l.insert(0,7) #вставка по индексу
print(l)
l.reverse() #развернуть


l.pop(0) #удаление по индексу
l.remove(1) #удаление первое вхождение елемента

print(l)

while 1 in l:
    l.remove(1)

print(l)
l.sort()
print(l)
l.clear()
print(l)