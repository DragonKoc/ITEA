FORMAT = 'pickle'  # 'json'


def get_serializer():
    if FORMAT == 'json':
        import json_ as serializer
    elif FORMAT == 'pickle':
        import pickle_ as serializer
    else:
        raise ImportError
    return serializer
