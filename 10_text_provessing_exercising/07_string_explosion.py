string = input()
new_string = ''
strength = 0

for i, ch in enumerate(string):
    if ch == '>':
        strength += int(string[i+1])
        new_string += '>'
    elif ch != '>' and strength > 0:
        strength -= 1
        continue
    else:
        new_string += ch


print(new_string)