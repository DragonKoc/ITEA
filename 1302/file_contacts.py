import pickle
contacts = {}


def load():
    try:
        with open('files/phone_list', 'rb') as f:
            return pickle.load(f)
    except FileNotFoundError:
        print('Ooops!!!')
        return {} #file

def save():
    with open('files/phone_list', 'wb') as f:
        pickle.dump(contacts, f)

def auto_save(f):
    def wrapper(*args, **kwargs):
        res = f (*args, **kwargs)
        save()
        return res
    return wrapper

