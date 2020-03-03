cities = ['Tula', 'Kiev', 'Toronto', 'Lviv', 1, 2, 6, 8, 3]


for i in cities:
    print(i)


try:
    cities.sort()

except TypeError:
    print('Error')
    try:
        for i in cities:
            print(str(i) + '*')
            if i in range(1, 10):
                print('deleted: ' + str(i))
                #cities.remove(i)

    except:
        print('error')


print(cities)
