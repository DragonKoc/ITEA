def bread_niz(f):
    def wrapper():
        f()
        print('\_____/')
    return wrapper

def bread_verh(f):
    def wrapper():
        print('/-------\\')
        f()
    return wrapper


#kolbasa = bread_verh(bread_niz(kolbasa))

@bread_niz
@bread_verh
def kolbasa():
    print('kolbas')

kolbasa()

