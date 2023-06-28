gifts_planned = input().strip().split()

while True:
    command = input()
    if command == 'No Money':
        break

    command = command.strip().split()

    if command[0] == 'OutOfStock':
        for index in range(len(gifts_planned)):
            if gifts_planned[index] == command[1]:
                gifts_planned[index] = 'None'

    elif command[0] == 'Required':
        for index in range(len(gifts_planned)):
            if command[2] == str(index):
                gifts_planned[index] = command[1]

    elif command[0] == 'JustInCase':
        gifts_planned[-1] = command[1]

result = []
for element in gifts_planned:
    if element != 'None':
        result.append(element)

print(' '.join(result))