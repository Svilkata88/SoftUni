from math import floor
def center_point(num1, num2, num3, num4):
    number1 = abs(num1) + abs(num2)
    number2 = abs(num3) + abs(num4)
    if number1 < number2:
        return f'({int(floor(num1))}, {int(floor(num2))})'
    return f'({int(floor(num3))}, {int(floor(num4))})'


num1, num2, num3, num4 = float(input()), float(input()), float(input()), float(input())
print(center_point(num1, num2, num3, num4))