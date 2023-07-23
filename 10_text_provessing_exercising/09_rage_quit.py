def set_count(string):
    string = [ch for ch in string if not ch.isnumeric()]
    b = [ch.lower() for ch in string if ch.isalpha()]
    c = [b.append(ch) for ch in string if not ch.isalnum()]
    return len(set(b))


string = input()
new_string = ''
current_string = ''
num = ''

for i in range(len(string)):
    if not string[i].isnumeric():
        current_string += string[i]
    else:
        num += string[i]
        if (i+1) in range(len(string)):
            if not string[i+1].isnumeric():
                new_string += current_string * int(num)
                current_string = ''
                num = ''
        else:
            new_string += current_string * int(num)

new_string = list(new_string)
new_string = [ch.upper() for ch in new_string]
new_string = ''.join(new_string)

print(f'Unique symbols used: {set_count(string)}')
print(new_string)
