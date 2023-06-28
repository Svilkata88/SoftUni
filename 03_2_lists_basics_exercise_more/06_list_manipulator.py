input_string = input().split()

while True:
    command = input().split()
    if command[0] == 'end':
        break
    if command[0] == 'exchange':
        command_int = int(command[1])
        if command_int < 0:
            print('Invalid index')
            continue
        elif len(input_string) <= command_int:
            print('Invalid index')
            continue
        else:
            for index in range(len(input_string) - 1, command_int, -1):
                input_string.insert(0, input_string.pop(-1))
    if command[0] == 'max':
        if command[1] == 'odd':
            new_list = []
            input_string = [int(ch) for ch in input_string]
            for value in input_string:
                if value % 2 != 0:
                    new_list.append(value)
            if not new_list:
                print('No matches')
                continue
            for index, value in enumerate(new_list):
                if value == max(new_list):
                    index_list = []
                    for i, element in enumerate(input_string):
                        if element == value:
                            index_list.append(i)
                    index_list = index_list[-1]
                    print(index_list)
                    break
        if command[1] == 'even':
            new_list = []
            input_string = [int(ch) for ch in input_string]
            for value in input_string:
                if value % 2 == 0:
                    new_list.append(value)
            if not new_list:
                print('No matches')
                continue
            for index, value in enumerate(new_list):
                if value == max(new_list):
                    index_list = []
                    for i, element in enumerate(input_string):
                        if element == value:
                            index_list.append(i)
                    index_list = index_list[-1]
                    print(index_list)
                    break
    if command[0] == 'min':
        if command[1] == 'odd':
            new_list = []
            input_string = [int(ch) for ch in input_string]
            for value in input_string:
                if value % 2 != 0:
                    new_list.append(value)
            if not new_list:
                print('No matches')
                continue
            for index, value in enumerate(new_list):
                if value == min(new_list):
                    index_list = []
                    for i, element in enumerate(input_string):
                        if element == value:
                            index_list.append(i)
                    print(index_list[-1])
                    break
        if command[1] == 'even':
            new_list = []
            input_string = [int(ch) for ch in input_string]
            for value in input_string:
                if value % 2 == 0 and value != 0:
                    new_list.append(value)
            if not new_list:
                print('No matches')
                continue
            for index, value in enumerate(new_list):
                if value == min(new_list):
                    index_list = []
                    for i, element in enumerate(input_string):
                        if element == value and element != 0:
                            index_list.append(i)
                    index_list = index_list[-1]
                    print(index_list)
                    break
    if command[0] == 'first':
        number = int(command[1])
        if number > len(input_string):
            print('Invalid count')
            continue
        if command[2] == 'even':
            new_list = []
            input_string = [int(ch) for ch in input_string]
            for element in input_string:
                if element % 2 == 0 and element != 0:
                    new_list.append(element)
            if number > (len(input_string)):
                print('Invalid count')
            elif len(new_list) > number:
                output = [new_list[num] for num in range(number)]
                print(output)
            else:
                print(new_list)
        if command[2] == 'odd':
            new_list = []
            input_string = [int(ch) for ch in input_string]
            for element in input_string:
                if element % 2 != 0 and element != 0:
                    new_list.append(element)
            if number > (len(input_string)):
                print('Invalid count')
            elif len(new_list) > number:
                output = [new_list[num] for num in range(number)]
                print(output)
            else:
                print(new_list)
    if command[0] == 'last':
        number = int(command[1])
        if number > len(input_string):
            print('Invalid count')
            continue
        if command[2] == 'even':
            new_list = []
            input_string = [int(ch) for ch in input_string]
            for element in input_string:
                if element % 2 == 0 and element != 0 :
                    new_list.append(element)
            output = [new_list[num] for num in range(len(new_list) - 1, -1, -1)]
            if len(output) > number:
                output_new = [output[num] for num in range(number)]
                output_new.reverse()
                print(output_new)
            else:
                print(output)
        if command[2] == 'odd':
            new_list = []
            input_string = [int(ch) for ch in input_string]
            for element in input_string:
                if element % 2 != 0:
                    new_list.append(element)
            output = [new_list[num] for num in range(len(new_list)-1, -1, -1)]
            if len(output) > number:
                output_new = [output[num] for num in range(number)]
                output_new.reverse()
                print(output_new)
            else:
                print(output)
print(input_string)
