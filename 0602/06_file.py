f = open("files/01",'wt')

#r - read
#w - whrite (if not exists whrite) >
#a - append >>
# +t кодирование

print(f)

f.write('Hello world\n')
f.write('Hello world\n')
f.write('Hello world\n')

f.flush() #сбрасывает на диск
print(f.tell()) #количество символов и побочка сбрасывает на диск
f.write('строка 4\n')
print(f.tell())

f.close() #закрывает файл

ff = open("files/01",'rt')
print(ff.read())
ff.close()


ff = open("files/01",'rt')
print(ff.read())


