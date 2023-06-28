num = int(input())
total_sum = 0

for number in range(1, num + 1):
    char = input()
    total_sum += ord(char)

print(f'The sum equals: {total_sum}')
