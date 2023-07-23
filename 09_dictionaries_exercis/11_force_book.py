force_book_data = {}
command = input()

while True:
    if command == 'Lumpawaroo':
        break
    if ' | ' in command:
        force, user = command.split(' | ')
        if force not in force_book_data:
            for element in force_book_data:
                if user in force_book_data[element]:
                    break
            else:
                force_book_data[force] = [user]

        elif user not in force_book_data[force]:
            for element in force_book_data:
                if user in force_book_data[element]:
                    break
            else:
                force_book_data[force].append(user)

    elif ' -> ' in command:
        force, user = command.split(' -> ')
        force, user = user, force

        flag = False
        for k, v in force_book_data.items():
            if user in v:
                force_book_data[k].remove(user)
                if force not in force_book_data:
                    force_book_data[force] = [user]
                else:
                    force_book_data[force].append(user)

                flag = True
                break
        if not flag:
            if force not in force_book_data:
                force_book_data[force] = [user]
            else:
                force_book_data[force].append(user)
        print(f'{user} joins the {force} side!')

    command = input()

for element in force_book_data:
    if len(force_book_data[element]) > 0:
        print(f'Side: {element}, Members: {len(force_book_data[element])}')
        for el in force_book_data[element]:
            print(f'! {el}')
