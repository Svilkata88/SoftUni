n_lines = int(input())

tank_capacity = 255

for i in range(n_lines):
    l_water = int(input())
    if l_water > tank_capacity:
        print(f'Insufficient capacity!')
        continue
    tank_capacity -= l_water
print(255 - tank_capacity)
