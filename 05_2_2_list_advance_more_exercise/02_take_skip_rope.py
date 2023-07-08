def take_skip(str_list, take_num, skip_num):
    taken_num = str_list[:take_num]
    return taken_num


def update_str_list(str_list, take_num, skip_num):
    str_list = str_list[take_num:]
    str_list = str_list[skip_num:]
    return str_list


string = input()
str_list = []
number_list = []

for letter in string:
    if letter.isnumeric():
        number_list.append(letter)
    else:
        str_list.append(letter)

number_list = [int(num) for num in number_list]

take_list = [number_list[num] for num in range(len(number_list)) if num % 2 == 0]
skip_list = [number_list[num] for num in range(len(number_list)) if num % 2 != 0]

result_list = []

for index in range(len(take_list)):
    take_num = take_list[index]
    skip_num = skip_list[index]
    taken_part = take_skip(str_list, take_num, skip_num)
    new_list = update_str_list(str_list, take_num, skip_num)
    str_list = new_list
    result_list.append(taken_part)

result_list = [''.join(ch) for ch in result_list]
print(''.join(result_list))