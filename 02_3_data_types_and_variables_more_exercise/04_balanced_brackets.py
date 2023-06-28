n_lines = int(input())
condition = False
counter = 0

for line in range(n_lines):
    string = input()
    if string == '(':
        counter += 1
        if counter < 2:
            condition = True
        else:
            condition = False
            break
    elif string == ')':
        if counter == 1:
            counter = 0
            condition = True
        else:
            condition = False
            break


if condition:
    print('BALANCED')
else:
    print('UNBALANCED')


