obj1 = {'abc': (1,2,3),123: 'qwerty'}

print(str(obj1))

import pickle

# load
# dump
# load_s serialize
# dump_s serialize

s= pickle.dumps(obj1)
print(s)

obj2 = pickle.loads(s)
print(obj2)
print(obj1 == obj2)


with open ('files/obj.pickle', 'wb') as f:
    pickle.dump(obj1,f)

with open ('files/obj.pickle', 'rb') as f:
    obj2 = pickle.load(f)

print(obj1 == obj2)