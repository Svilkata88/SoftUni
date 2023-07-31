def insert_space(index):
    new_message = list(concealed_message)
    new_message.insert(index, ' ')
    new_message = ''.join(new_message)
    return new_message


def reverse(substring):
    if substring in concealed_message:
        old_part = concealed_message.replace(substring, '', 1)
        new_string = old_part + substring[::-1]
        return new_string


def change_all(substring, replacement):
    new_string = concealed_message.replace(substring, replacement)
    return new_string


concealed_message = input()

commands = input()
while commands != 'Reveal':
    command, *others = commands.split(':|:')
    if command == 'InsertSpace':
        index = int(others[0])
        concealed_message = insert_space(index)
        print(concealed_message)

    elif command == 'Reverse':
        substring = others[0]
        if reverse(substring) is not None:
            concealed_message = reverse(substring)
            print(concealed_message)
        else:
            print('error')

    elif command == 'ChangeAll':
        substring, replacement = others
        concealed_message = change_all(substring, replacement)
        print(concealed_message)

    commands = input()

print(f'You have a new text message: {concealed_message}')