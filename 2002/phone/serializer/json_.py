import json

class Json:
    def load(self):
        try:
            with open("./phonebook.json", "rt") as f:
                return json.load(f)
        except FileNotFoundError:
            return {}


    def save(self,obj):
        with open("./phonebook.json", "wt") as f:
            json.dump(obj, f)
