def take_odd(string):
    new_password = ''
    for index in range(len(string)):
        if index % 2 != 0:
            new_password += string[index]
    return new_password


def cut(string, index, length):
    index_end = index + length
    part_1 = string[:index]
    part_2 = string[index_end:]
    result = part_1 + part_2
    return result


def substitute(string, substring, substitution):
    result = string.replace(substring, substitution)
    return result


string = input()

commands = input().split()
while commands[0] != 'Done':

    command, *other = commands

    if command == 'TakeOdd':
        string = take_odd(string)
        print(string)

    elif command == 'Cut':
        index, length = other
        index, length = int(index), int(length)
        string = cut(string, index, length)
        print(string)

    elif command == 'Substitute':
        substring, substitution = other
        if substring in string:
            string = substitute(string, substring, substitution)
            print(string)
        else:
            print('Nothing to replace!')

    commands = input().split()

print(f'Your password is: {string}')

