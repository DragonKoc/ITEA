from random import randrange

duration = randrange(100)


for number in range(duration):
    sleep = 365 * 24 * 60 * 60 * 1000
    if sleep == duration:
        Life = True
    else:
        Life = False

def Lifes(Life):
    if Life == True:
        return print("continue")
    else:
        return print('Die')

Lifes(Life)


def factorial (n):
    pr=1
    for i in range(2,n+1):
        pr = pr*i
    print(pr)
factorial(3)

if 5>7:
    def pri():
        print('TRUE')
else:
    def pri():
        print('FALSE')

pri()

a=int(input())
if a%2 ==0:
    print('ok')
else:
    print('no')
