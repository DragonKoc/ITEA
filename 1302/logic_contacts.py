#import file_contacts as file
#import decor_file as file
import decor_file

serializer = decor_file.get_serializer('pickle')
contacts = serializer.load()

#contacts = {}


def contac_exists(f):
    def wrapper(name, *args):
        if name not in contacts:
            raise KeyError('Contact doesn`t exists')
        return f(name, *args)
    return wrapper


def create(name,phone):
    if name  in contacts:
        raise KeyError('Contact already exists')
    contacts[name] = phone
    serializer.save()

@contac_exists
def read(name):
    return contacts[name]

@contac_exists
def update(name,phone):
    contacts[name] = phone
    serializer.save()

@contac_exists
def delete(name):
    del contacts[name]
    file.save()

def create_contact():
    name = input('Name?', )
    phone = input('Phone?',)
    create(name,phone)


def read_contact():
    name = input('Name?', )
    print(read(name))

def update_contact():
    name = input('Name?', )
    phone = input('Phone?', )
    #contacts[name] = phone
    update(name,phone)

def del_contact():
    name = input('Name?', )
    #del contacts[name]
    delete(name)

def default():
    print('Incorrect input')