def min_max_sum(string):
    numbers_int= [int(ch) for ch in string]
    min_numbers = min(numbers_int)
    max_numbers = max(numbers_int)
    sum_numbers = sum(numbers_int)
    print(f'The minimum number is {min_numbers}')
    print(f'The maximum number is {max_numbers}')
    print(f'The sum number is: {sum_numbers}')


string = input().split()
min_max_sum(string)