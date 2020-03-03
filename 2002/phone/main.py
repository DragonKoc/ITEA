import phonebook
import settings

serializer = settings.get_serializer()
contacts = phonebook.Contacts(serializer)

def create_contact():
    name = input("Name? ")
    phone = input("Phone? ")
    contacts.create(name, phone)


def read_contact():
    name = input("Name? ")
    print(contacts.read(name))


def update_contact():
    name = input("Name? ")
    phone = input("Phone? ")
    contacts.update(name, phone)


def delete_contact():
    name = input("Name? ")
    contacts.delete(name)


def default():
    print("Incorrect input")


actions = {
    'c': create_contact,
    'r': read_contact,
    'u': update_contact,
    'd': delete_contact,
    'q': exit,
}

while True:
    print("""Actions:
c - create
r - read
u - update
d - delete
q - quit""")
    action = input().lower()
    try:
        actions.get(action, default)()
    except KeyError as e:
        print(e.args[0])
