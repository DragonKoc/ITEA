import settings


serializer = settings.get_serializer()
contacts = serializer.load()


def contact_exists(f):
    def wrapper(name, *args):
        if name not in contacts:
            raise KeyError("Contact doesn't exist")
        return f(name, *args)

    return wrapper


def autosave(f):
    def wrapper(*args, **kwargs):
        res = f(*args, **kwargs)
        serializer.save(contacts)
        return res

    return wrapper


@autosave
def create(name, phone):
    if name in contacts:
        raise KeyError("Contact already exists")
    contacts[name] = phone


@contact_exists
def read(name):
    return contacts[name]


@autosave
@contact_exists
def update(name, phone):
    contacts[name] = phone


@autosave
@contact_exists
def delete(name):
    del contacts[name]
