from math import floor, sqrt


def center_point(num1, num2, num3, num4):
    number1 = abs(num1) + abs(num2)
    number2 = abs(num3) + abs(num4)
    if number1 < number2:
        return f'({int(floor(num1))}, {int(floor(num2))})({int(floor(num3))}, {int(floor(num4))})'
    return f'({int(floor(num3))}, {int(floor(num4))})({int(floor(num1))}, {int(floor(num2))})'


def longer_line(num1,num2,num3,num4,num5,num6,num7,num8):
    line1 = sqrt((num3 + num1)**2 + (num4-num2)**2)
    line2 = sqrt((num7 + num5)**2 + (num8-num6)**2)
    if line1 > line2:
        return center_point(num1, num2, num3, num4)
    return center_point(num5, num6, num7, num8)


num1, num2, num3, num4, num5, num6, num7, num8 = float(input()), float(input()), float(input()), float(input()), \
                                                float(input()), float(input()), float(input()), float(input())

print(longer_line(num1, num2, num3, num4, num5, num6, num7, num8))