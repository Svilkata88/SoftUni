level_of_fire = input().split('#')
water = int(input())
total_fire = 0
total_effort = 0
valid_cells = []
cell = False

for elements in level_of_fire:
    elements = elements.split(' = ')
    if elements[0] == 'High':
        if 81 <= int(elements[1]) <= 125:
            cell = True
        else:
            continue
    elif elements[0] == 'Medium':
        if 51 <= int(elements[1]) <= 80:
            cell = True
        else:
            continue
    elif elements[0] == 'Low':
        if 1 <= int(elements[1]) <= 50:
            cell = True
        else:
            continue

    if cell:
        cell_value_int = int(elements[1])
        if cell_value_int <= water:
            water -= cell_value_int
            total_fire += cell_value_int
            total_effort += cell_value_int * 0.25
            valid_cells.append(cell_value_int)

print('Cells:')
for element in valid_cells:
    print(f' - {element}')
print(f'Effort: {total_effort:.2f}')
print(f'Total Fire: {total_fire}')