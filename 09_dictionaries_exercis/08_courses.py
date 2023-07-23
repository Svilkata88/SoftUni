courses = {}

while True:
    command = input()
    if command == 'end':
        break
    course, name = command.split(' : ')
    if course not in courses:
        courses[course] = [name]
    else:
        courses[course].append(name)

for k, v in courses.items():
    print(f'{k}: {len(v)}')
    for index in range(len(v)):
        print(f'-- {v[index]}')