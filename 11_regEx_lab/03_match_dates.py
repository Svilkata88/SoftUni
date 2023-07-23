import re

raw_string = input()

pattern = r'(\d{2})([-.\/])([A-Z][a-z]{2})\2(\d{4})'

matches = re.findall(pattern, raw_string)


for match in matches:
    day = match[0]
    separator = match[1]
    month = match[2]
    year = match[3]

    print(f'Day: {day}, Month: {month}, Year: {year}')
