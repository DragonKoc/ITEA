FORMAT = 'pickle'  # 'json'


def get_serializer():
    if FORMAT == 'json':
       from serializer import json_ as serializer
    elif FORMAT == 'pickle':
        from serializer import pickle_ as serializer
    else:
        raise ImportError
    return serializer
