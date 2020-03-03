client = {
    'name': '',
    'surname': '',
    'phone': ['phone1','phone2'],
    'operator': ''
}

print(client)


client['rank'] = 'admin'

print(client)
del client['rank']
print(client)

all_client = []

# for x in range(0,10):
#     all_client.append(client) #clone

for i in all_client:
    print(i)

for x in range(0,10):
     all_client.append(client.copy()) #clone

print(all_client)



all_client[5]['name'] = 'Koc'

for i in all_client:
    print(i)