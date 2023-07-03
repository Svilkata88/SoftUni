def factorial(num1, num2):
    total1 = 1
    total2 = 1
    for n in range(1, num1 + 1):
        total1 *= n
    total = 1
    for n in range(1, num2 + 1):
        total2 *= n
    result = total1 / total2
    output = f'{result:.2f}'
    return output


num1, num2 = int(input()), int(input())
print(factorial(num1, num2))