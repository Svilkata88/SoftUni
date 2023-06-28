working_day_events = input().split('|')
starting_energy = 100
starting_coins = 100
current_energy = starting_energy
current_coins = starting_coins
flag = True

for event in working_day_events:
    type_event, number = event.split('-')

    if type_event == 'rest':
        starting_energy = current_energy
        if current_energy < 100:
            current_energy += int(number)
            if current_energy > 100:
                current_energy = 100
            print(f'You gained {current_energy-starting_energy} energy.')
            print(f'Current energy: {current_energy}.')
        else:
            number = 0
            print(f'You gained {number} energy.')
            print(f'Current energy: {current_energy}.')
    elif type_event == 'order':
        if current_energy >= 30:
            current_energy -= 30
            current_coins += int(number)
            print(f'You earned {number} coins.')
        else:
            current_energy += 50
            print('You had to rest!')
    else:
        if current_coins >= int(number):
            current_coins -= int(number)
            print(f'You bought {type_event}.')
        else:
            print(f'Closed! Cannot afford {type_event}.')
            flag = False
            break

if flag:
    print('Day completed!')
    print(f'Coins: {current_coins}')
    print(f'Energy: {current_energy}')