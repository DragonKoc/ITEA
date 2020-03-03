contacts = {}

while True:
    print("""Action:
          c - create
          r - read
          u - update
          d - delete
          q - quit""")
    action = input().lower()
    if action == 'q':
        break
    elif action == 'c':
        name = input('Name?',)
        phone = input('Phone?,')
        if name in contacts:
            print('Contact already exists')
        else:
            contacts[name] = phone
    elif action == 'r':
        name = input('Name?',)
        if name not in contacts:
            print('Contact doesn`t exists')
        else:
            print(contacts[name])
    elif action == 'u':
        name = input('Name?',)
        phone = input('Phone?',)
        contacts[name] = phone
    elif action == 'd':
        name = input('Name?',)
        del contacts[name]

   #c print(contacts)
