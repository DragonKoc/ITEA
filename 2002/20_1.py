class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def __repr__(self): #object see
        return f"Person({self.name=},{self.age=})"
    def __str__(self): #first
        return f"<{self.name}, {self.age}>"

p = Person('Bill',23)

print(p)
#print(dir(object)) #magic methods
print(p.__repr__())
#print(repr(p))

p1 = Person('Jon',25)
p2 = Person('Jon',25)

print(p1==p2)

class Persons:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def __repr__(self): #object see
        return f"Person({self.name=},{self.age=})"
    def __str__(self): #first
        return f"<{self.name}, {self.age}>"
    def __eq__(self, other):
        if hasattr(other, 'name') and hasattr(other,'age'):
            return self.name == other.name and self.age == other.age
        if isinstance(other, str):
            return self.name == other
        return NotImplemented

p3 = Persons('Jon',25)
p4 = Persons('Jon',25)
print(p3 == p4)

print('***********************')

print(isinstance('John', str))
print(hasattr(p1,'name')) #обнаружить поле обьекта
print(hasattr('John','name')) #обнаружить поле обьекта

print('***********************')

p5 = Persons('Jon',25)
p6 = Persons('Jon',25)

print(p5 == p6)
print(p5 == 'Jon')

print('Jon' == p5)
print('Jon'.__eq__(p5))

print('Jon' == 1)


