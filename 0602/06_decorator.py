#  некий набор функций для одинаковых действий
# подключение отключение БД / логгирование

def get_area(x):
    return x**2

def scale(f):
    def wrapper(x):
        x *= 100
        res = f(x) # тут помнит про старую get_area
        return res
    return wrapper

print('before')
print(get_area(5))
print('decor')
get_area = scale(get_area) #декорирование
print('after')
print(get_area(5))
print('xxxxx')


@scale
def get_area(x):
    return x*x

print(get_area(5))

@scale #декоратор в декораторе
@scale
def get_area(x):
    return x*x

print(get_area(5))

print('##### DECOR ######')

# позиционные параметры
# именованые параметры

def log(y):
    def wrapper (*args,**kwargs):
        print(y.__name__, "<--", args, kwargs )
        res = y(*args,**kwargs)
        print(y.__name__,'-->',res)
    return wrapper


@log
def thisisfunction(x,y):
    return x + y

thisisfunction(2,3)
thisisfunction(2,y=5)


import functools

def log2(y):
    @functools.wraps(y)
    def wrapper (*args,**kwargs):
        print(y.__name__, "<--", args, kwargs )
        res = y(*args,**kwargs)
        print(y.__name__,'-->',res)
        return res
    return wrapper

@log2
def add(x,y):
    """Add x and y"""
    return  x + y

add(5,5)
