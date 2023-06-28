input_string = input().split()


def exchange(command, input_string):
    command_int = int(command[1])
    if command_int < 0:
        print('Invalid index')
    elif len(input_string) < command_int:
        print('Invalid index')
    else:
        for index in range(len(input_string) - 1, command_int, -1):
            input_string.insert(0, input_string.pop(-1))
            return input_string
# return split list after the given index and exchanges the places of the two resulting sub-lists
# parameters: command(user input), input_string(given list)


def odd(command, input_string):
    if command[1] == 'odd':
        new_list = []
        input_string = [int(ch) for ch in input_string]
        for value in input_string:
            if value % 2 != 0:
                new_list.append(value)
        if not new_list:
            print('No matches')
        for index, value in enumerate(new_list):
            if value == max(new_list):
                index_list = []
                for i, element in enumerate(input_string):
                    if element == value:
                        index_list.append(i)
                    if len(index_list) == 0:
                        continue
                    elif len(index_list) > 1:
                        index_list = index_list[-1]
                    elif len(index_list) == 1:
                        index_list = index_list[0]
                    print(index_list)
                    break
# print index of the max/min argument in the given list.
# parameters: command(user input), input_string(given list), min/max(user decide min or max argument if the list needs)


def even(command, input_string, max):
    if command[0] == 'even':
        new_list = []
        input_string = [int(ch) for ch in input_string]
        for value in input_string:
            if value % 2 == 0:
                new_list.append(value)
        if not new_list:
            print('No matches')
        for index, value in enumerate(new_list):
            if value == max(new_list):
                index_list = []
                for i, element in enumerate(input_string):
                    if element == value:
                        index_list.append(i)
                    if len(index_list) == 0:
                        index_list = index_list
                    elif len(index_list) > 1:
                        index_list = index_list[-1]
                    elif len(index_list) == 1:
                        index_list = index_list[0]
                    print(index_list)
                    break


while True:
    command = input().split()
    if command[0] == 'end':
        break
    if command[0] == 'exchange':
        print(exchange(command, input_string))
    if command[0] == 'even':
        even(command, input_string, max)



