def f():
    a = 5
    def g():
        def h():
            print(a+1)
        print(a+1)
    g()

f()