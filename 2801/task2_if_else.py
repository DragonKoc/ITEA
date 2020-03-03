# task2

# a=2
# b=1
#
#
# if a<b:
#     res=b
#     print(res)
# elif a>b:
#     if 1==1:
#         print('1=1')
#     else:
#         print('1!=1')
#     res = a
#     print(res)

a = int(input())
b = int(input())
c = int(input())
t = 0

if a>b:
    t=a
    if t>c:
        print(t)
    else:
        print(c)
else:
    t=b
    if t>c:
        print(t)
    else:
        print(c)

        # >> > b = 2 if a > 6 else 3
        # >> > b
        # 3
        # >> > b = 2 if a < 6 else 3
        # >> > b
        # 2



