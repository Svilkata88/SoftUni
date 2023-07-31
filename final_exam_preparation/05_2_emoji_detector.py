import re

text = input()
digits = []
cool_emojis = []
pattern = r'([:]{2}|[*]{2})([A-Z][a-z]{2,})\1'

for ch in text:
    if ch.isdigit():
        digits.append(ch)

digits = [int(ch) for ch in digits]
cool_threshold = 1

for digit in digits:
    cool_threshold *= digit

matches = re.finditer(pattern, text)
for match in matches:
    emoji = match.group(2)
    coolness = 0
    for ch in emoji:
        coolness += ord(ch)
    if coolness > cool_threshold:
        cool_emojis.append(match.group())

matches = re.finditer(pattern, text)
matches_count = 0
for ch in matches:
    matches_count += 1

print(f'Cool threshold: {cool_threshold}')
print(f'{matches_count} emojis found in the text. The cool ones are:')
for emoji in cool_emojis:
    print(emoji)
