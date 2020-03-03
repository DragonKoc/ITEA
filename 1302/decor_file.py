
def get_serializer(FORMAT = 'pickle'):
    if FORMAT == 'json':
        import file_json as serializer
    elif FORMAT == 'pickle':
        import file_contacts as serializer
    else:
        raise ImportError
    return serializer

