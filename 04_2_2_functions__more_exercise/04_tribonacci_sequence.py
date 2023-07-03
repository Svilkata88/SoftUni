def tribonacci_number(num):
    number = 0
    numbers_list = [1, 0, 0]
    output = '1'
    for n in range(1, num):
        the_number = sum(numbers_list)
        numbers_list.insert(0, the_number)
        del numbers_list[-1]
        the_number = str(the_number)
        output += f' {the_number}'
    return output


num = int(input())
print(tribonacci_number(num))