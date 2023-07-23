products = {}

while True:
    command = input().split()
    if command[0] == 'buy':
        break

    product, price, quantity = command
    price = float(price)
    quantity = int(quantity)

    if product not in products:
        products[product] = [0, 0]
    products[product][0] = price
    products[product][1] += quantity

for k,v in products.items():
    print(f'{k} -> {v[0]*v[1]:.2f}')