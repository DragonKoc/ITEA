class A:
    def __init__(self):
        self.a = 0            # public interface
        self._donttouchme = 0 # var of class (not interface, best dont touch)
        self.__secret = 0     #

a = A()
print(a.a)
a.a = 3
print(a.a)
#
print(a._donttouchme)
print(vars(a))
a.__secret