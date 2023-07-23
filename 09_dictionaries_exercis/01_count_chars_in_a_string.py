text = input()
letter_dict = {}

text = text.replace(' ', '')
for letter in text:
    if letter not in letter_dict:
        letter_dict[letter] = 0
    letter_dict[letter] += 1


for element in letter_dict.items():
    print(f'{element[0]} -> {element[1]}')