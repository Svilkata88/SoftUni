def blacklist(friends, name):
    global blacklisted_counter
    if name in friends:
        friends[friends.index(name)] = 'Blacklisted'
        blacklisted_counter += 1
        return f'{name} was blacklisted.'
    blacklisted_counter = blacklisted_counter
    return f'{name} was not found.'


def error(friends, index):
    global lost_counter
    if index in range(0, len(friends)):
        name = f'{friends[index]} was lost due to an error.'
        friends[index] = 'Lost'
        lost_counter += 1
        return name


def change(friends, index, name):
    if index in range(0, len(friends)):
        new_name = f'{friends[index]} changed his username to {name}.'
        friends[index] = name
        return new_name


friends = input().split(', ')
command = ''
blacklisted_counter = 0
lost_counter = 0

while True:
    command = input().split()
    if command[0] == 'Report':
        break
    if command[0] == 'Blacklist':
        print(blacklist(friends, command[1]))
    elif command[0] == 'Error':
        if friends[int(command[1])] in friends and 'Blacklisted' not in friends[int(command[1])] and\
                'Lost' not in friends[int(command[1])]:
            print(error(friends, int(command[1])))
        else:
            lost_counter = lost_counter
    elif command[0] == 'Change':
        if int(command[1]) in range(0, len(friends)):
            print(change(friends, int(command[1]), command[2]))

print(f'Blacklisted names: {blacklisted_counter}')
print(f'Lost names: {lost_counter}')
print(' '.join(friends))