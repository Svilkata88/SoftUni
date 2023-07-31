import re

text_string = input()

pattern = r'([#@])([A-Za-z]{3,})\1(\1)([A-Za-z]{3,})\1'
pairs = []
mirror_words = []
matches = re.finditer(pattern, text_string)

for match in matches:
    current_match = f'{match.group(2)} <=> {match.group(4)}'
    if match.group(2) == match.group(4)[::-1]:
        if current_match not in mirror_words:
            mirror_words.append(current_match)
    if match.group() not in pairs:
        pairs.append(match.group())

if len(pairs) == 0:
    print('No word pairs found!')
    print('No mirror words!')
elif len(pairs) > 0:
    print(f'{len(pairs)} word pairs found!')
    if len(mirror_words) > 0:
        print('The mirror words are:')
        print(', '.join(mirror_words))
    else:
        print('No mirror words!')
