def sum_numbers(num1, num2):
    result = num1 + num2
    return result


def subtract(num1, num2, num3):
    result = sum_numbers(num1, num2) - num3
    return result


num1, num2, num3 = int(input()), int(input()), int(input())
print(subtract(num1, num2, num3))