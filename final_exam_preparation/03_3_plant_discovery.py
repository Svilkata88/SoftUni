n_inputs = int(input())
plants = {}

for _ in range(n_inputs):
    plant_found = input().split('<->')
    plant, rarity = plant_found
    rarity = int(rarity)
    plants[plant] = [rarity]

commands = input().split(': ')
while commands[0] != 'Exhibition':
    command, others = commands
    if command == 'Rate':
        plant, rating = others.split(' - ')
        rating = int(rating)
        if plant in plants:
            plants[plant].append(rating)
        else:
            print('error')

    elif command == 'Update':
        plant, new_rarity = others.split(' - ')
        new_rarity = int(new_rarity)
        if plant in plants:
            plants[plant][0] = new_rarity
        else:
            print('error')

    elif command == 'Reset':
        plant = others
        if plant in plants:
            plants[plant] = [plants[plant][0]]
        else:
            print(f'error')

    commands = input().split(': ')

print('Plants for the exhibition:')
for plant, statistics in plants.items():
    ratings = statistics[1:]
    length_ratings = len(ratings)
    if length_ratings > 0:
        print(f'- {plant}; Rarity: {statistics[0]}; Rating: {sum(ratings) / length_ratings:.2f}')
    else:
        print(f'- {plant}; Rarity: {statistics[0]}; Rating: {0:.2f}')