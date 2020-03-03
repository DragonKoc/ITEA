import json


def load():
    try:
        with open("phonebook.json", "rt") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}


def save(obj):
    with open("phonebook.json", "wt") as f:
        json.dump(obj, f)
