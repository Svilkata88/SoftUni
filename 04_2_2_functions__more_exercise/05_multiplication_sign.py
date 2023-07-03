def multiplication_sign(num1, num2, num3):
    numbers_list = [num1, num2, num3]
    result = None
    if 0 in numbers_list:
        result = 'zero'
        return result
    for n in numbers_list:
        if n < 0:
            result = 'negative'
            break
        else:
            result = 'positive'
    return result


num1, num2, num3 = int(input()), int(input()), int(input())
print(multiplication_sign(num1, num2, num3))