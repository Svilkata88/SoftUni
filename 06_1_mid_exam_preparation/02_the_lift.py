people_waiting = int(input())
lift_state = input().split()
place_in_wagon = 4
filled_wagons = []

lift_state = [int(wagons) for wagons in lift_state]

for index in range(len(lift_state)):
    if people_waiting < 0:
        [filled_wagons.append(0) for num in range(len(lift_state) - len(filled_wagons))]
        print('The lift has empty spots!')
        print(*filled_wagons, sep=' ')
        break
    if people_waiting == 0:
        print(*lift_state, sep=' ')
        break
    free_space = place_in_wagon - lift_state[index]
    if people_waiting > free_space or people_waiting == 0:
        people_waiting -= free_space
        place_filled = place_in_wagon
        filled_wagons.append(place_filled)
    elif people_waiting == free_space:
        filled_wagons.append(place_filled)
        print(*filled_wagons, sep=' ')
        break
    else:
        place_filled = lift_state[index] + people_waiting
        filled_wagons.append(place_filled)
        if len(filled_wagons) < len(lift_state):
            [filled_wagons.append(0) for num in range(len(lift_state) - len(filled_wagons))]
        print(f'The lift has empty spots!\n{" ".join([str(num) for num in filled_wagons])}')
        break


else:
    print(f'There isn\'t enough space! {people_waiting} people in a queue!\n\
{" ".join([str(num) for num in filled_wagons])}')










