wagons = int(input())


def add_people(num):
    wagons_list[-1] += num
    return wagons_list

def insert_people(index, num):
    wagons_list[index] += num
    return wagons_list

def leave_people(index, num):
    wagons_list[index] -= num
    return wagons_list

wagons_list = list('0' * wagons)
wagons_list = [int(ch) for ch in wagons_list]

while True:
    command = input().split()
    if command[0] == 'End':
        break
    if command[0] == 'add':
        add_people(int(command[1]))
    elif command[0] == 'insert':
        insert_people(int(command[1]), int(command[2]))
    elif command[0] == 'leave':
        leave_people(int(command[1]), int(command[2]))

print(wagons_list)