import re

string = input()

pattern = r'\b[A-Z][a-z]+\s[A-Z][a-z]+\b'

matches = re.findall(pattern, string)
print(matches)
[print(match) for match in matches]