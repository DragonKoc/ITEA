# import csv
# a = raw_input('Vvedite nomer ')
# reader = csv.reader(open("data2.csv", "rb"), delimiter=';')
# name = None
# for row in reader:
#     if a == row[2]:
#         name = row[0], row[1]
# if name:
#     print name
# else:
#     print 'Phone not found'



f = lambda x:2*x
print(f(2) )
f = lambda :1234
print(f())