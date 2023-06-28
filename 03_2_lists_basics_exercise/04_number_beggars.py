integers_string_list = input().split(', ')
count_of_beggars = int(input())
result = []
start_index = 0

while start_index < count_of_beggars:
    sum_of_elements = 0
    for element in range(start_index, len(integers_string_list), count_of_beggars):
        sum_of_elements += int(integers_string_list[element])

    result.append(int(sum_of_elements))
    start_index += 1


print(result)

