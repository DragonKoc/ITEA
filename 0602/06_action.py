def f_a():
    print('A')

def f_b():
    print('B')

def f_c():
    print('C')


action = 'a'

actions = {'a':f_a, 'b':f_b, 'c':f_c}

print(actions[action])
actions[action]()

action = 'x'
def default():
    print('Default')

actions.get(action,default)()