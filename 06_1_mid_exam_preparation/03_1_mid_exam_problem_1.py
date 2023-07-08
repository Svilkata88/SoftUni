needed_experiences = float(input())
battles_count = int(input())
total_experience = 0
battles_counter = 0

for battle in range(1, battles_count+1):
    experience = float(input())

    if battle % 15 == 0:
        experience *= 1.05
    elif battle % 5 == 0:
        experience *= 0.9
    elif battle % 3 == 0:
        experience *= 1.15
    else:
        experience = experience
    total_experience += experience
    battles_counter += 1
    if total_experience >= needed_experiences:
        print(f'Player successfully collected his needed experience for {battles_counter} battles.')
        break
else:
    print(f'Player was not able to collect the needed experience, {needed_experiences - total_experience:.2f}'
          f' more needed.')