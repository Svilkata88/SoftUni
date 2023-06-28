string_of_numbers = input().split()
left_car_time = 0
right_car_time = 0

#numbers_list = [int(num) for num in string_of_numbers]

finish_line = len(string_of_numbers) // 2

for index in range(0, finish_line, 1):
    if string_of_numbers[index] == '0':
        left_car_time *= 0.8
        continue
    left_car = string_of_numbers[index]
    left_car_time += int(left_car)

for index in range(len(string_of_numbers) - 1, finish_line, -1):
    if string_of_numbers[index] == '0':
        right_car_time *= 0.8
        continue
    right_car = string_of_numbers[index]
    right_car_time += int(right_car)

if left_car_time > right_car_time:
    print(f'The winner is right with total time: {right_car_time:.1f}')
else:
    print(f'The winner is left with total time: {left_car_time:.1f}')
