string = input().split()
palindrome = input()
palindrome_list = []
pal_counter = 0

for word in string:
    if word == word[::-1]:
        palindrome_list.append(word)
        pal_counter = palindrome_list.count(palindrome)

print(palindrome_list)
print(f'Found palindrome {pal_counter} times')
