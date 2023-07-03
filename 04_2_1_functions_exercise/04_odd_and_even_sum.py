def odd_even_sum(num):
    odd_sum = 0
    even_sum = 0
    for n in str(num):
        n = int(n)
        if n % 2 == 0:
            even_sum += n
        elif n % 2 != 0:
            odd_sum += n
    return f'Odd sum = {odd_sum}, Even sum = {even_sum}'


num1 = int(input())
print(odd_even_sum(num1))
