# name = input('Please input your name: ' ,)
#
# print('Privet ' + name)
#
# num1 = int(input('Enter x: '))
# num2 = input('Enter y: ')
#
# summa = num1 + int(num2)
# print(summa)

message = ''

while message != 'secret':
    message = input('Password: ',)
    if message == 'secret':
        break
    print('Try another')
print('Password correct!')

mylist = []
msg = ''

while msg != 'stop':
    msg = input('Enter new intem', )
    mylist.append(msg)

print(mylist)