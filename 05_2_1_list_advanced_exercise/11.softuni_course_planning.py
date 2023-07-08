def add(initial_schedule, lessonTitle):
    if lessonTitle not in initial_schedule:
        initial_schedule.append(lessonTitle)

def insert(initial_schedule, lessonTitle, index):
    if lessonTitle not in initial_schedule:
        initial_schedule.insert(index, lessonTitle)
    return initial_schedule


def remove(initial_schedule, lessonTitle):
    if lessonTitle in initial_schedule:
        if initial_schedule.index(lessonTitle) + 1 in range(len(initial_schedule)):
            if 'Exercise' in initial_schedule[initial_schedule.index(lessonTitle)+1]:
                initial_schedule.pop((initial_schedule.index(lessonTitle) + 1))
        initial_schedule.remove(lessonTitle)
    return initial_schedule


def swap(initial_schedule, lessonTitle1, lessonTitle2):
    if lessonTitle1 and lessonTitle2 in initial_schedule:
        el1_index = initial_schedule.index(lessonTitle1)
        el2_index = initial_schedule.index(lessonTitle2)
        lesson1_exercise = False
        lesson2_exercise = False
        if el1_index + 1 in range(len(initial_schedule)):
            lesson1_exercise = 'Exercise' in initial_schedule[el1_index + 1]
        if el2_index + 1 in range(len(initial_schedule)):
            lesson2_exercise = 'Exercise' in initial_schedule[el2_index + 1]

        initial_schedule[el1_index], initial_schedule[el2_index] = \
            initial_schedule[el2_index], initial_schedule[el1_index]

        if lesson1_exercise and lesson2_exercise:
            initial_schedule[el1_index + 1], initial_schedule[el2_index + 1] = \
                initial_schedule[el2_index + 1], initial_schedule[el1_index + 1]
        elif lesson1_exercise and not lesson2_exercise:
            initial_schedule.insert(el2_index+1, initial_schedule.pop(el1_index+1))
        elif lesson2_exercise and not lesson1_exercise:
            initial_schedule.insert(el1_index+1, initial_schedule.pop(el2_index+1))

    return initial_schedule


def exercise(initial_schedule, lessonTitle):
    if lessonTitle in initial_schedule and f'{lessonTitle}-Exercise' not in initial_schedule:
        initial_schedule.insert((initial_schedule.index(lessonTitle) + 1), f'{lessonTitle}-Exercise')
    elif lessonTitle not in initial_schedule:
        initial_schedule.append(lessonTitle)
        initial_schedule.append(f'{lessonTitle}-Exercise')
    return initial_schedule


initial_schedule = input().split(', ')


while True:
    command = input().split(':')
    if command[0] == 'course start':
        break
    elif command[0] == 'Add':
        add(initial_schedule, command[1])
    elif command[0] == 'Insert':
        insert(initial_schedule, command[1], int(command[2]))
    elif command[0] == 'Remove':
        remove(initial_schedule, command[1])
    elif command[0] == 'Swap':
        swap(initial_schedule, command[1], command[2])
    elif command[0] == 'Exercise':
        exercise(initial_schedule, command[1])

[print(f'{index + 1}.{lesson}') for index, lesson in enumerate(initial_schedule)]