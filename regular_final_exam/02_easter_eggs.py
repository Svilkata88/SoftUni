import re

text_string = input()
pattern = r'(([#@]+)([a-z]{3,})([#@]+))([^0-9a-zA-Z]*)([\/]+([\d]+)[\/]+)'

matches = re.finditer(pattern, text_string)

for match in matches:
    color = match.group(3)
    amount = match.group(7)
    if int(amount) > 0:
        print(f'You found {amount} {color} eggs!')