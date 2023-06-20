total_coffee = 0

while True:
    task = input()
    if task == 'END':
        break

    if task == task.lower():
        if task == 'coding' or task == 'dog' or task == 'cat' or task == 'movie':
            total_coffee += 1
    elif task == task.upper():
        task = task.lower()
        if task == 'coding' or task == 'dog' or task == 'cat' or task == 'movie':
            total_coffee += 2
    else:
        continue

if total_coffee <= 5:
    print(total_coffee)
else:
    print('You need extra sleep')