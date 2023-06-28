number = input().split()
string = input()
counter = 0
total  = 0
searched_word = ''

for n in number:
    for num in n:
        num = int(num)
        counter += num

    for index in range(len(string)):
        if index == counter % len(string):
            searched_word += string[index]
            b = string[index+1:]
            c = string[:index]
            string = f'{c}{b}'
            total += index
            counter = 0
            break

print(searched_word)

