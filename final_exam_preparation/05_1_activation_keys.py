def contains(substring):
    if substring in act_key:
        return f'{act_key} contains {substring}'
    return f'Substring not found!'


def flip(action, start_index, end_index):
    if action == 'Upper':
        part_1 = act_key[:start_index]
        part_2 = act_key[end_index:]
        sub_str = act_key[start_index:end_index]
        sub_str = sub_str.upper()
        new_string = part_1 + sub_str + part_2
        return new_string
    elif action == 'Lower':
        part_1 = act_key[:start_index]
        part_2 = act_key[end_index:]
        sub_str = act_key[start_index:end_index]
        sub_str = sub_str.lower()
        new_string = part_1 + sub_str + part_2
        return new_string


def slice(start_index, end_index):
    del_part = act_key[start_index:end_index]
    new_string = act_key.replace(del_part, '', 1)
    return new_string


act_key = input()

commands = input()

while commands != 'Generate':
    command, *others = commands.split('>>>')
    if command == 'Contains':
        substring = others[0]
        print(contains(substring))
    elif command == 'Flip':
        action, start_index, end_index = others
        start_index = int(start_index)
        end_index = int(end_index)
        act_key = flip(action, start_index, end_index)
        print(act_key)
    elif command == 'Slice':
        start_index, end_index = others
        start_index = int(start_index)
        end_index = int(end_index)
        act_key = slice(start_index, end_index)
        print(act_key)

    commands = input()

print(f'Your activation key is: {act_key}')