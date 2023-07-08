n_rooms = int(input())
total_free_chairs = 0
total_needed_chairs = 0
for room in range(1, n_rooms + 1):
    chairs, visitors = input().split()
    n_chairs = len(chairs)
    visitors = int(visitors)
    needed_chairs = visitors - n_chairs
    if needed_chairs <= 0:
        free_chairs = n_chairs - visitors
        total_free_chairs += free_chairs
    else:
        total_needed_chairs += abs(needed_chairs)
        print(f'{needed_chairs} more chairs needed in room {room}')

difference = total_free_chairs - total_needed_chairs
if difference >= 0:
    print(f'Game On, {total_free_chairs} free chairs left')

