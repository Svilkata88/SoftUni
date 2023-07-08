string = input().split()
numbers = []
output = []
ch = ''

for word in string:
    for i in range(len(word)):
        if word[i].isnumeric():
            numbers.append(word[i])
        else:
            numbers = int(''.join(numbers))
            ch = word[i]
            word = word[:i] + word[-1] + word[i+1:]
            word = word[i:]
            word = f'{word[:-1]}{ch}'
            new_word = f'{chr(numbers)}{word}'
            output.append(new_word)
            numbers = []
            break

print(' '.join(output))
