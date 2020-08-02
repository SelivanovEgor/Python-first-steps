ids = {'user1': [213, 213, 213, 15, 213],
       'user2': [54, 54, 119, 119, 119],
       'user3': [213, 98, 98, 35],
       'user4': [11, 98, 24, 213]}
unic = []
for user in ids:
    for num in ids.get(user):
        if num not in unic:
            unic.append(num)
print(unic)
