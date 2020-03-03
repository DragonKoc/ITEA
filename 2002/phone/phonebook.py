def contact_exists(f):
    def wrapper(self,name, *args):
        if name not in self.contacts:
            raise KeyError("Contact doesn't exist")
        return f(self,name, *args)

    return wrapper


def autosave(f):
    def wrapper(self,*args, **kwargs):
        res = f(self,*args, **kwargs)
        self.serializer.save(self.contacts)
        return res
    return wrapper

class Contacts:
    def __init__(self,serializer):
        self.serializer = serializer
        self.contacts = self.serializer.load()

    @autosave
    def create(self,name, phone):
        if name in self.contacts:
            raise KeyError("Contact already exists")
        self.contacts[name] = phone


    @contact_exists
    def read(self,name):
        return self.contacts[name]


    @autosave
    @contact_exists
    def update(self,name, phone):
        self.contacts[name] = phone


    @autosave
    @contact_exists
    def delete(self,name):
        del self.contacts[name]


