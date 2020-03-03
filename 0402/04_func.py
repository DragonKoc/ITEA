# def func():
#     x = 0
#     def gg(x):
#         return x * 2
#     return gg
#
# print(func()(4))
# print(func())
#
# def f(x):
#     def g(y):
#         return x*y
#     return  g
#
# print(f(2)(3))
x = ''
def name(x):
    x = input('Please enter yor name: ',)
    print('Hello '+ x)


name('tttt')

def summa(x,y):
    s = x + y
    return s

print(summa(33,22))

s1= 10
for i in range(1, s1+1):
     for j in range(i, i*s1+1, i):
         print(j, end='\t')
     print()


def create_person(name, phone):
        person = {
            'name': name,
            'phone': phone
        }
        return person


client1 = create_person('Vasya', '2222222')
client2 = create_person('Billy', '3333333')

print(client1)

a = [1, 2, 3, 4, 6, 7, 99, 88, 999]
max = 0
for i in a:
    if i > max:
        max = i
print(max)

name_i = input()
phone_i = input()


def person_all(name='', phone='', action='q'):
    def p_c(name='', phone=''):
        person = {
            'name': name,
            'phone': phone
        }
    return person
    def p_r(name='', phone=''):
        if name not in person:
            print('Contact doesn`t exists')
        else:
            print(person[name])
