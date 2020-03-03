class Table:
    def __init__(self,w=60, l=100):
        self.w = w            # public interface
        self.l= l             # var of class (not interface, best dont touch)
    def get_area(self):
        return self.w*self.l

    def get2(f):
        def wrapper(self):
          print('tut decorator')
          f(self)
        return wrapper


class TableWithDrawer(Table):
    def __init__(self,w,l,drawer_area):
        super().__init__(w,l)
        self.drawer_area = drawer_area

    @Table.get2
    def get_area(self):
        return super().get_area() + self.drawer_area


t = TableWithDrawer(50,100,123)

t.get_area()

#print(t.get_area())

