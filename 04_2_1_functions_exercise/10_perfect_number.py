def perfect_number(a):
    a = int(input())
    divisors = []
    for i in range(1, a):
        if a % i == 0:
            divisors.append(i)

    if sum(divisors) == a:
        print('We have a perfect number!')
    else:
        print('It\'s not so perfect.')

perfect_number(6)