FORMAT = 'pickle'  # 'json'


def get_serializer():
    if FORMAT == 'json':
        from serializer import json_
        serializer = json_.Json()
    elif FORMAT == 'pickle':
        from serializer import pickle_
        serializer = pickle_.Pickle()
    else:
        raise ImportError
    return serializer