def all_between_two_ch(a, b):
    a = ord(a)
    b = ord(b)
    total_string = ''

    for num in range(a + 1, b):
        num = chr(num)
        total_string += f' {num}'
    total_string = total_string[1:]
    print(total_string)


a, b = input(), input()
all_between_two_ch(a, b)
