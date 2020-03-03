class MyList(list):
    def sum(self):
        a = 0
        for item in self:
            a += item
        return a

l = MyList([1,2,3])
print(l)

l.append(5)
print(l)

print(l.sum())

print('****list2******')

class Mylist2:
    def __init__(self,l):
        self._l = list(l)
    def __repr__(self):
        return repr(self._l)

# ll = Mylist2([1,2,4])
# print(ll)
#
# l1 = Mylist2(ll)
# print(l1)

lll = Mylist2('abc')
print(lll)

print('****list3******')

class Mylist3:
    def __init__(self,l):
        self._l = list(l)
    def __repr__(self):
        return repr(self._l)
    def __len__(self):
        return len(self._l)

l4 = Mylist3([1,2,3])
print(l4)