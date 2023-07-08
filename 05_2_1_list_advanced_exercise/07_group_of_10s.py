numbers = input().split(', ')

max_value = 10

while len(numbers) > 0:
    group_numbers = [int(num) for num in numbers if int(num) <= max_value]
    numbers = [int(num) for num in numbers if int(num) not in group_numbers]
    print(f'Group of {max_value}\'s: {group_numbers}')
    max_value += 10