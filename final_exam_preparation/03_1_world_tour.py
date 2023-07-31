def add_stop(index, new_stop):
    if index in range(len(stops)):
        old_part_1 = stops[:index]
        old_part_2 = stops[index:]
        new_string = old_part_1 + new_stop + old_part_2
        return new_string
    return stops

def remove_stop(start_index, end_index):
    if start_index in range(len(stops)) and end_index in range(len(stops)):
        cutted_string = stops[start_index:end_index+1]
        new_string = stops.replace(cutted_string, '', 1)
        return new_string
    return stops


def switch(old_string, new_string):
    if old_string in stops:
        new_string = stops.replace(old_string, new_string)
        return new_string
    return stops


stops = input()

commands = input()
command, *others = commands.split(':')
while command != 'Travel':
    if command == 'Add Stop':
        index, new_stop = others
        index =int(index)
        stops = add_stop(index, new_stop)
        print(stops)

    elif command == 'Remove Stop':
        start_index, end_index = others
        start_index = int(start_index)
        end_index = int(end_index)
        stops = remove_stop(start_index, end_index)
        print(stops)

    elif command == 'Switch':
        old_string, new_string = others
        stops = switch(old_string, new_string)
        print(stops)

    commands = input()
    command, *others = commands.split(':')

print(f'Ready for world tour! Planned stops: {stops}')
