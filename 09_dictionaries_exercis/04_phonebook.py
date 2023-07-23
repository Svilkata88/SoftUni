phonebook = {}

while True:
    entry = input()
    if entry.isdigit():
        break
    name, number = entry.split('-')
    phonebook[name] = number

for index in range(int(entry)):
    name = input()
    if name in phonebook:
        print(f'{name} -> {phonebook[name]}')
    else:
        print(f'Contact {name} does not exist.')
