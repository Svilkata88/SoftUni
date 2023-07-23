string = input().strip().split()
total_sum = 0
rng = range(ord('A'), ord('Z'))
rng_lower = range(ord('a'), ord('z'))

for el in string:
    middle_sum = 0
    number = int(el[1:-1])

    letter_position = ord(el[0].upper()) - 64
    if el[0].isupper():
        middle_sum += number / letter_position

        letter_position = ord(el[-1].upper()) - 64
        if el[-1].isupper():
            middle_sum -= letter_position
        elif el[-1].islower():
            middle_sum += letter_position
        total_sum += middle_sum

    elif el[0].islower():
        middle_sum += number * letter_position

        letter_position = ord(el[-1].upper()) - 64
        if el[-1].isupper():
            middle_sum -= letter_position
        elif el[-1].islower():
            middle_sum += letter_position
        total_sum += middle_sum

print(f'{total_sum:.2f}')