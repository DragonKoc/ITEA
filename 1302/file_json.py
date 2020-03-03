import json
contacts = {}


def load():
    try:
        with open('files/phone_list', 'rt') as f:
            return json.load(f)
    except FileNotFoundError:
        print('Ooops!!!')
        return {} #file

def save():
    with open('files/phone_list', 'wt') as f:
        json.dump(contacts, f)

def auto_save(f):
    def wrapper(*args, **kwargs):
        res = f (*args, **kwargs)
        save()
        return res
    return wrapper

