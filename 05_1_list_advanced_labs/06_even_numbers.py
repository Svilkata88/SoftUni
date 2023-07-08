numbers = input().split(', ')

numbers_list = list(map(int, numbers))
even_numbers = list(map(lambda x: x if numbers_list[x] % 2 ==0 else 'No', range(len(numbers_list))))
even_numbers = list(filter(lambda x: x != 'No', even_numbers))
print(even_numbers)