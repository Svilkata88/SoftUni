string = input()
new_string = ''

for i, ch in enumerate(string):
    if ch != string[i-1] or i == 0:
        new_string += ch

print(new_string)
