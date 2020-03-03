f = open('files/01', 'rt')

print(f.read())
print(f.tell())
print(f.read(),'end')
f.close()



f = open('files/01', 'rt')
print(f.readline())
print(f.readline())
print(f.readline())
print(f.readline())
print(f.readline())
print(f.readline())
print(f.readline())
print(f.readline())
print(f.readline(),'end')

#readline

f = open('files/01', 'rt')
for line in f:
    print(line , end ='')


# copy file import shutil
# 3.8
f = open('files/01', 'rt')
while line := f.readline():
    print(line)


# def f():
#     f = None
#     x = 0
#     try:
#         f = open('files/01', 'rt')
#
#
#     finally:
#         if f is not None:
#             f.close()
#     return x


#надежный способ
with open('files/01', 'rt') as f:
    for line in f:
        print(line)

print(f.close())

ff = open("files/01",'rt')

for line in ff:
     print(line + 'ololol')
ff.close()

