numbers = input().split()
k = int(input())
killed = []
n = 1


while True:

    for num in range(0, len(numbers), k):
        if len(numbers) <= k:
            k = abs(len(numbers) - k)
            n = 1
        if num == 0:
            continue
        killed.append(numbers[num - n])
        del numbers[num - n]
        n += 1

        print(numbers)
        print(killed)
        print()
    n = 1