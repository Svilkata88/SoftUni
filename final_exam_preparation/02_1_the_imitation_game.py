def move(encrypted_message, n_letters):
    cutted_part = encrypted_message[:n_letters]
    part_left = encrypted_message[n_letters:]
    encrypted_message = part_left + cutted_part
    return encrypted_message


def insert(encrypted_message, index, value):
    part_1 = encrypted_message[:index]
    part_2 = encrypted_message[index:]
    new_string = part_1 + value + part_2
    return new_string


def change_all(encrypted_message, substring, replacement):
    new_string = encrypted_message.replace(substring, replacement)
    return new_string


encrypted_message = input()
command = input()

while command != 'Decode':
    operation, *others = command.split('|')
    if operation == 'Move':
        n_letters = others[0]
        n_letters = int(n_letters)
        encrypted_message = move(encrypted_message, n_letters)

    elif operation == 'Insert':
        index, value = others
        index = int(index)
        encrypted_message = insert(encrypted_message, index, value)

    elif operation == 'ChangeAll':
        substring, replacement = others
        encrypted_message = change_all(encrypted_message, substring, replacement)

    command = input()

print(f'The decrypted message is: {encrypted_message}')