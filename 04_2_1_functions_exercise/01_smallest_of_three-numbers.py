def min_number(num1, num2, num3):
    min_num = min(num1, num2, num3)
    return min_num


num1, num2, num3 = int(input()), int(input()), int(input())

print(min_number(num1, num2, num3))