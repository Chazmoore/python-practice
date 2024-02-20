# user_0 = {
#     'username': 'efermi',
#     'first': 'enrico',
#     'last:': 'fermi'
# }

# print(user_0)

# user_0 = {
#     'username': 'efermi',
#     'first': 'enrico',
#     'last:': 'fermi'
# }

# for key, value in user_0.items():
#     print(f'\nKey: {key}')
#     print(f"Value: {value}")

users = {
    'aeistein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princrton',
    },

    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
    },
}

for username, user_info in users.items():
    print(f"\nUsername: {username}")
    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info['location']

    print(f"\tFull name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")