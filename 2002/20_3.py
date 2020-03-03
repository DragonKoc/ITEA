class ReprMixin:
    # только методы без состояний
    def __repr__(self):
        return "{}({})".format(
            self.__class__.__name__,
            ','.join(f"{name}={value}" for name , value in vars(self).items())
        )

class EqMixin:
    def __eq__(self, other):
        #vars - все поля и все значения
        return vars(self) ==vars(other)

class Person(ReprMixin, EqMixin):
    def __init__(self,name,age): # состояние!!!!
        self.name = name
        self.age = age
    # def __repr__(self): #object see
    #     return f"Person({self.name=},{self.age=})"
    def __str__(self): #first
        return f"<{self.name}, {self.age}>"
    # def __eq__(self, other):
    #     if hasattr(other, 'name') and hasattr(other,'age'):
    #         return self.name == other.name and self.age == other.age
    #     if isinstance(other, str):
    #         return self.name == other
    #     return NotImplemented
    def __lt__(self, other):
        return self.name < other.name

p = Person('Bill',32)
print(p)


p1 = Person('John',23)
p2 = Person('John',23)

print(p1==p2)
