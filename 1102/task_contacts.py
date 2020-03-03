contacts = {}

def work():
    print("""Action:
          c - create
          r - read
          u - update
          d - delete
          q - quit""")


#def contacts_all(name='', phone='', action='q'):

def p_c(name='', phone='' ):
        name = input('Name', )
        phone = input('phone', )
        if name in contacts:
            print('Contact already exists')
        else:
            contacts['name'] = name
            contacts['phone'] = phone

        print(contacts)

def p_r(name='', phone='', action='r'):
        name = input('Name', )
        if name not in contacts['name']:
            print('Contact doesn`t exists')
        else:
            print(contacts)

def p_u(name='', phone='', action='q'):
        name = input('Name', )
        if name not in contacts['name']:
            print('Contact doesn`t exists')
        else:
            contacts['phone'] = phone

def p_d(name='',phone='', action='d'):
    name = input('Name?', )
    del contacts[name]

def p_q():
    quit = False


quit = True

while quit == True:

    work()
    action = input().lower()
    if action == 'q':
        p_q()
        break
    elif action == 'c':
        p_c()
    elif action == 'r':
        p_r()
    elif action == 'u':
        p_u()
    elif action == 'd':
        p_d()


