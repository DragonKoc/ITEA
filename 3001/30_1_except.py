# excep errors

a=0

try:
#   raise ValueError('My code error')
   b=5/a

except ZeroDivisionError:
    print('ZDE')
except NameError:
    print('NE')
    exit()
except Exception as e:
    print(e)
else:
    print('b = ', b)
finally:
    print('Finally')

print('The end')

#a=1
# b =  5.0
# Finally
# The end

#a=0
# ZDE
# Finally
# The end

##a
# NE
# Finally

#a='0'
# Traceback (most recent call last):
#   File "/Users/dragon/Dev/Github/ITEA/3001/30_1.py", line 6, in <module>
#     b=5/a
# TypeError: unsupported operand type(s) for /: 'int' and 'str'
# Finally
