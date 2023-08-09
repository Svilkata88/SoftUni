def test():
    for word in words:
        if word in definitions:
            print(f'{word}:')
            for el in definitions[word]:
                print(f' -{el}')


def hand_over():
    key_words = []
    for word in definitions:
        key_words.append(word)
    print(' '.join(key_words))


string_input = input().split(' | ')
definitions = {}

for element in string_input:
    key, val = element.split(': ')
    if key not in definitions:
        definitions[key] = [val]
    elif val not in definitions[key]:
        definitions[key].append(val)
    else:
        continue

words = input().strip().split(' | ')

command = input()
if command == 'Test':
    test()
elif command == 'Hand Over':
    hand_over()