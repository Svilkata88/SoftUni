n = int(input())

for string in range(n):
    S = str(input())
    for i in S:
        if i == ',' or i == '.' or i == '_':
            print(f'{S} is not pure!')
            break
    else:
        print(f'{S} is pure.')