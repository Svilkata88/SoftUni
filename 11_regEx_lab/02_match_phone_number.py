import re

raw_string = input()

pattern = r"(\+359)([-| ])(2)\2(\d{3})\2(\d{4})\b"

matches = re.finditer(pattern, raw_string)
valid_numbers = []
for el in matches:
    valid_numbers.append(el.group())

print(', '.join(valid_numbers))
