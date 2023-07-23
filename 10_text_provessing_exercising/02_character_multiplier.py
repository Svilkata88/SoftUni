def string_multiplication(string1, string2):
    mid_sum = 0
    if len(string1) > len(string2):
        for index in range(len(string2)):
            mid_sum += ord(string1[index]) * ord(string2[index])
        for index in range(len(string1)-len(string2)):
            num = ord(string1[index+len(string2)])
            mid_sum += num
    elif len(string2) > len(string1):
        for index in range(len(string1)):
            mid_sum += ord(string1[index]) * ord(string2[index])
        for index in range(len(string2) - len(string1)):
            num = ord(string2[index + len(string1)])
            mid_sum += num
    else:
        for index in range(len(string2)):
            mid_sum += ord(string1[index]) * ord(string2[index])
    return mid_sum

two_strings = input().split()
string1, string2 = two_strings

print(string_multiplication(string1, string2))