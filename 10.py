user = {'name': 'john', 'age': 28}
print(user['name'])

user1 = dict(name = 'William', age=30)
print(user1)

# in dictionaries we can store numbers, lists, dictionaries etc..

user_info = {
    'name': 'John',
    'age': 28,
    'favoruite_movies': ['real steel', 'iron man'],
    'favoruite_tunes': ['awakening', 'fairy tale']
}

users = {
    'user1': {
        'name': 'John',
        'age': 28
    },
    'user2': {
        'name': 'william',
        'age': 30
    }
}

if 'John' in users['user1'].values():
    print(True)
else:
    print(False)

if 'name' in users['user1']:
    print(True)
else:
    print(False)

for i in users.values():
    print(i)

user_items = user_info.items()
print(user_items)

for key, value in user_info.items():
    print(f'key is {key} and value is {value}')

# adding data
user_info['fav_songs'] = ['tum se', 'kaho na pyar hai']
print(user_info['fav_songs'])

# Pop Method
popped_item = user_info.pop('favoruite_tunes')
print(popped_item)

# Pop item
popped_item = user_info.popitem() #remove the last key, value pair
print(popped_item)

# update
more_info = {'state': 'AP', 'hobbies': ['thinking', 'listening music']}
user_info.update(more_info)
print(user_info)

# from keys
d = {'name': 'unknown', 'age': 'unknown'}

print(d)

d = dict.fromkeys(['name', 'age', 'height'], '8')

print(d) # All of them will have the value of 8

e = dict.fromkeys(('weight', 'occupation'), 10)

print(e)

e.update(d)

print(e)

d = dict.fromkeys(range(1,11), 'unknown')

print(d)