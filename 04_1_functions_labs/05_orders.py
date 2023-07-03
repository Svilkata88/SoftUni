def order_calculator(product, price):
    prices_dic = {'coffee': 1.50, 'water': 1.00, 'coke': 1.40, 'snacks': 2.00}
    for k, v in prices_dic.items():
        if k == product:
            output = v * price
            return f'{output:.2f}'

product = input()
price = float(input())
print(order_calculator(product, price))




