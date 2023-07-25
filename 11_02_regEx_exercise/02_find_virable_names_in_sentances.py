import re

line = input()

pattern = r'(\b_)([A-Za-z0-9]+)\b'

matches = re.finditer(pattern, line)
result = []
for match in matches:
    result.append(match.group(2))

print(','.join(result))