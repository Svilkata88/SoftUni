string = input().split()

new_string = [word for word in string if len(word) % 2 == 0]
for word in new_string:
    print(word)
