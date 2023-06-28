num = int(input())

for a in range(num):
    for b in range(num):
        for c in range(num):
            print(f'{chr(97+a)}{chr(97+b)}{chr(97+c)}')