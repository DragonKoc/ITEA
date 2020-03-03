class Table:
    def __init__(self,w=60, l=100):
        self.w = w            # public interface
        self.l= l             # var of class (not interface, best dont touch)
    def get_area(self):
        return self.w*self.l


class TableWithDrawer(Table):
    def __init__(self,w,l,drawer_area):
        super().__init__(w,l)
        self.drawer_area = drawer_area

    def get_area(self):
        return super().get_area() + self.drawer_area

class RoundTable:
    def __init__(self,r):
        self.r = r
    def get_area(self):
        return 3.14*self.r*self.r


tables = [Table(),TableWithDrawer(50,120,123), Table(60,140)]
print(tables)

tables.append((RoundTable(100)))

print(tables)

print(sum([tables.get_area() for tables in tables]))

#SOLID
#Robert Martin Гибкая разработка программ
#Patterns