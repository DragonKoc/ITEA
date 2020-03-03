obj1 = {123: 'abc', 'qwe' : (1, 2, 3) }

print(obj1)

import pickle

#dump - save on disk
#dumps - save in string

s = pickle.dumps(obj1)
print(s)
obj2 = pickle.loads(s)
print(obj1 == obj2)

print('****************')

#serialize
with open('files/object.pickle', 'wb') as f:
    pickle.dump(obj1,f)

#deserialize
with open('files/object.pickle', 'rb') as f:
    obj2 = pickle.load(f)


print(obj2)

import json
ss = json.dumps(obj1)
print(ss)
