def plunder(town, people_killed, gold):
    cities_data[town][0] -= people_killed
    cities_data[town][1] -= gold
    print(f'{town} plundered! {gold} gold stolen, {people_killed} citizens killed.')
    if cities_data[town][0] <= 0 or cities_data[town][1] <= 0:
        del cities_data[town]
        print(f'{town} has been wiped off the map!')


def prosper(town, gold):
    if gold < 0:
        print(f'Gold added cannot be a negative number!')
    else:
        cities_data[town][1] += gold
        print(f'{gold} gold added to the city treasury. {town} now has {cities_data[town][1]} gold.')


cities_data = {}

command_cities = input()
while command_cities != 'Sail':
    town, population, gold = command_cities.split('||')
    population = int(population)
    gold = int(gold)
    if town in cities_data:
        cities_data[town][0] += population
        cities_data[town][1] += gold
    else:
        cities_data[town] = [population, gold]
    command_cities = input()

command_events = input()
while command_events != 'End':
    event, *other = command_events.split('=>')
    if event == 'Plunder':
        town, people_killed, gold = other
        people_killed = int(people_killed)
        gold = int(gold)
        plunder(town, people_killed, gold)

    elif event == 'Prosper':
        town, gold = other
        gold = int(gold)
        prosper(town, gold)

    command_events = input()

if len(cities_data) > 0:
    print(f'Ahoy, Captain! There are {len(cities_data)} wealthy settlements to go to:')
    for city, data in cities_data.items():
        print(f'{city} -> Population: {data[0]} citizens, Gold: {data[1]} kg')
else:
    print('Ahoy, Captain! All targets have been plundered and destroyed!')