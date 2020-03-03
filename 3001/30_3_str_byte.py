print('aaa\naaaa')
print("aaa'aaa\"aaaa") #\ экранирование
print('AC\\\\DC')
print('c:\new\file')

print(r'c:\new\file') #raw

print('''aaaaaaa
      aaaaa
        aaaaa''')

print(len('football'))
print('football'[0])  #0=1 symbol
print('football'[-1]) #end of string

print('football'[0:4]) #==print('football'[:4])
print('football'[4:])  #c 4 to end
print('football'[-3:]) #3 from end
print('football'[2:-2])
print('football'[::2]) #kagdiy vtoroy
print('football'[::-1]) #razvernut

print('f'*5)

print('foot' in 'football') #True
print(not 'foot' in 'football') #False
print('foot' not in 'football') #False

name = 'Bill'
age = 23
print('Name: '+name + '; age: '+str(age)) #HARD
print('Name: %s; age: %s' % (name,age))
print('Name: {}; age: {}'.format(name,age))
print(f'Name: {name}; age: {age}')


#UNICODE in Python
# zяyю
#1bite, 2byte, 1byte, 2byte
print('\xc4')

hi = 'Привет!'.encode('utf8') #from UNICODE to UTF8
print(type(hi)) #type bytes
print(hi.decode('utf8')) #to UNICODE from UTF8

print(dir(hi))
print(help("".endswith))


