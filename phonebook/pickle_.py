import pickle


def load():
    try:
        with open("phonebook.pickle", "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return {}


def save(obj):
    with open("phonebook.pickle", "wb") as f:
        pickle.dump(obj, f)
