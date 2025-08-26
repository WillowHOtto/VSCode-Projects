libraries = ['pandas', 'numpy', 'flask', 'django', 'fastapi', 'requests', 'matplotlib', 'seaborn', 'scikit-learn', 'tensorflow']
print(libraries)

for lib in libraries:
    print(lib)

print(f'There are {len(libraries)} things in the list.')

first_item = libraries[0]
last_item = libraries[-1] #fun!
print(f'First item in list: {first_item}, Last item in list: {last_item}')

# User interaction to select a library
user_numb = input('Enter the number of the library you want to see (1-10):')
index = int(user_numb) - 1
print(f'You selected: {libraries[index]}')