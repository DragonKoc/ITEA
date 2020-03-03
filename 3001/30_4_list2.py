cities = ['New York', 'Moscow', 'Kiev', 'new Deli', 'Toronto']

print(cities.index('Kiev')) #position of index
print(cities[2]) #index of position
print(cities[-2])
print(cities[3].title())
print(tuple(cities))

cities[1] = 'Tula'
print(cities)

cities.append('Lviv')
print(cities)
cities.extend([1,2,6,8,3])
print(cities)
cities.insert(1,'Gorod')
print(cities)
del cities[:2]
print(cities)
cities.pop(2)
print(cities)
print('****************')





