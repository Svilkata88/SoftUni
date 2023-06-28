num = int(input())
prime = True

for n in range(2, num):
    if num % n == 0:
        prime = False
        break
print(prime)
