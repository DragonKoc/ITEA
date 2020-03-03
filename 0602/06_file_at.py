f = open('files/01', 'at')
print(f.tell())

f.write('String5\n')
f.write('String6\n')
f.close()