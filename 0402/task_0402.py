# телефонный справочник
# контакты
# искать
# обновлять
# удалять


person = {'name': '', 'phone' : ''}



exi1 = 'n'
while exi1 == 'n':

    a = input('What you do?',)

    print('Person keys now')
    print(person.keys())
    print('Person values')
    print(person.values())

    if a == 'i':
        print('Who add?')
        b = input('Name', )
        p = input('phone',)
        person['name']=b
        person['phone'] = p
    elif a == 'u':
        print('Who update?')
        b = input('Name', )
        p = input('phone',)
        person['name'] = b
        person['phone'] = p
    elif a == 'd':
        print('Who kill?')
        b = input('Name', )
        p = input('phone',)
        del person[b]
        del person[p]

    # if a == 'i':
    #     person['name']=b
    #     person['phone'] = p
    # elif a == 'u':
    #     person['name'] = b
    #     person['phone'] = p
    # elif a == 'd':
    #     del person[b]
    #     del person[p]

    e = input('you end?',)
    if e == 'y':
        break
    else:
        print(person)






