import re

input_line = input()

patter = r'\s(([a-z0-9]+[a-z0-9\.\_\-*]+)@([a-z\-?]+)(\.[a-z\-?]+)+)\b'

matches = re.findall(patter, input_line)

for match in matches:
    print(match[0])
