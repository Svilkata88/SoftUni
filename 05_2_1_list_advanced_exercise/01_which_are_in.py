string1 = input().split(', ')
string2 = input().split(', ')

new_list = []
for word in string1:
    for word1 in string2:
        if word in word1:
            new_list.append(word)
            break

print(new_list)