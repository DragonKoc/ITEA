cities = ['Tula', 1, 2, 'Kiev', 'Toronto', 'Lviv', 1, 2, 6, 8, 3]
try:
    cities.sort()

except TypeError:
    print('Error')
    try:
        for i in cities:
            print(i)
            if i in range(1,6):
                print(i)
                cities.remove(i)

    except  ValueError:
        print('error')


print(cities)