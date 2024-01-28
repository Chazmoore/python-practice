# favorite_languages = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'rust',
#     'phil': 'python',
# }
# # print(favorite_languages)

# language = favorite_languages['sarah'].title()
# print(f"Sarah's favorite language is {language}.")

# favorite_languages = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'rust',
#     'phil': 'python',
# }

# for name, language in favorite_languages.items():
#     print(f"{name.title()}'s favorite language is {language.title()}.")

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
}

for name in favorite_languages.keys():
    print(name.title())