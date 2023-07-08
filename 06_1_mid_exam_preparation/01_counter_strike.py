energy = int(input())
battles_won = 0

while True:
    distance = input()
    if distance == 'End of battle':
        print(f'Won battles: {battles_won}. Energy left: {energy}')
        break
    if energy <= 0 or int(distance) > energy:
        print(f'Not enough energy! Game ends with {battles_won} won battles and {energy} energy')
        break

    energy -= int(distance)
    battles_won += 1
    if battles_won % 3 == 0:
        energy += battles_won

