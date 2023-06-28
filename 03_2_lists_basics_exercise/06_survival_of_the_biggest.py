numbers_list = input().split()
count_of_numbers_to_remove = int(input())
numbers_list_int = []
numbers_list_str = []

for num in numbers_list:
    numbers_list_int.append(int(num))

for _ in range(count_of_numbers_to_remove):
    numbers_list_int.remove(min(numbers_list_int))

for num in numbers_list_int:
    numbers_list_str.append(str(num))

output = ', '.join(numbers_list_str)
print(output)
