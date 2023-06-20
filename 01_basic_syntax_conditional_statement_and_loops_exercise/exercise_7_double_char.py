

while True:
    output = ''
    string = input()
    if string == 'End':
        break

    if string == 'SoftUni':
        continue

    for i in string:
        output += i * 2
    print (output)