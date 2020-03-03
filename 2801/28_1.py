# print('Hello World')
# print(type(123/3))
# print(5//2)     #целочисленное
# print(5%2)      #остаточное
# print(2**4)     #степень
#
# r=input('R? ')
# r=float(r)
# s=3.14*r**2
#
# print('S=',s)


for i in range(1,20, 2):
    print(i)
    if i == 5:
        continue
    elif i == 9:
        break
    print('end of loop')
print('END')
