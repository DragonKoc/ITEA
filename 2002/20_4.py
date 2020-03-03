# сверху вниз, слева направо
# если вызвали супер то вызывать по всей иерархии
#

class A:
    def __init__(self,**kwargs):
        print('A')
        super().__init__(**kwargs)

class B(A):
    def __init__(self,**kwargs):
        print('B')
        super().__init__(**kwargs)


class C(A):
    def __init__(self,**kwargs):
        print('C')
        super().__init__(**kwargs)

class D(B,C):
    def __init__(self,**kwargs):
        print('D')
        super().__init__(**kwargs)

D()

