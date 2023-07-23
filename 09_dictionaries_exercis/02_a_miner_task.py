command = input()
new_dict = {}

while True:
    if command == 'stop':
        break
    resource = int(input())

    if command not in new_dict:
        new_dict[command] = 0
    new_dict[command] += resource
    command = input()

for k, v in new_dict.items():
    print(f'{k} -> {v}')
