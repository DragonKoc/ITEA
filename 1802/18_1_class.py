class Table:
#    pass
    def set_w(self,w):
        print(self)
        self.w = w

table1 = Table()
table2 = Table()

table1.w = 100

print(vars(table1))
print(vars(table2))

table = Table()
table.set_w(100)
print(table.w)

print('**********TRIX1************')
class Tables():
    w = 101

tw = Tables()
print(tw.w)

print(vars(tw))

print('**********TRIX2************')


class Table3:
    def get_area(self):
        return self.w*self.l

t3 = Table3()


print('**********TRIX3************')

class Table4():
    def __init__(self,w=0,l=0): #magic method
        self.w = w
        self.l = l
    def get_are(self):
        return self.w*self.l

table4 = Table4(50,100)
print(vars(table4))

print(table4.get_are())

