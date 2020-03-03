import logic_contacts as logic

#contacts = {}

actions = {'c': logic.create_contact,
          'r' : logic.read_contact,
          'u' : logic.update_contact,
          'd' : logic.del_contact,
          'q' : exit,}

while True:
    print("""Action:
          c - create
          r - read
          u - update
          d - delete
          q - quit""")


    action = input().lower()
    try:
        actions.get(action, logic.default)()
    except KeyError as e:
        print(e.args[0])
