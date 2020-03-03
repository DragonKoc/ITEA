import random

secret=random.randint(1,10)
attempts = 0

while attempts<5:
    try:
        guess = int(input('?'))
    except ValueError:
        print('Incorect')
        attempts += 1
        continue
    if secret == guess:
        print('Ok!')
        break
    if secret > guess:
        print('>')
    else:
        print('<')
    attempts +=1
else:
    print('You looser')
