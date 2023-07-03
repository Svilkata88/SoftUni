def calculations(operator, x, y):
    operators = {
                 "multiply": (lambda x, y: x * y),
                 "divide": (lambda x, y: x / y),
                 "add": (lambda x, y: x + y),
                 "subtract": (lambda x, y: x-y)
    }
    for k, v in operators.items():
        if k == operator:
            output = v(x, y)
            return int(output)


operator, x, y = input(), int(input()), int(input())
print(calculations(operator, x, y))





