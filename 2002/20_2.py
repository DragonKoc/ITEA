class Person:
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
    def __lt__(self, other):
        return self.name < other.name


l = [Person('John',32), Person('Bill',43),Person('Mary',32)]
#l.sort() # TypeError

#print(l.sort(key=lambda x: x.name))
print(l)
l.sort()
print(l)