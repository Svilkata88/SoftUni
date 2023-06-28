items = input().strip().split('|')
budget = float(input())
new_profit_prices = []
budget_left = budget
profit = 0
total_sum = 0

for item in items:
    price_validation = False
    type_product, price = item.split('->')
    price = float(price)
    if type_product == 'Clothes':
        if price <= 50.00:
            price_validation = True
    elif type_product == 'Shoes':
        if price <= 35.00:
            price_validation = True
    elif type_product == 'Accessories':
        if price <= 20.50:
            price_validation = True
    else:
        continue

    if price_validation:
        if budget_left >= price:
            budget_left -= price
            new_profit_prices.append(float(f'{price * 1.40:.2f}'))
            profit += new_profit_prices[-1] - price
        else:
            continue

total_sum = sum(new_profit_prices) + budget_left

#print(*new_profit_prices, sep=' ')
#for item in new_profit_prices:
    #print(f'{item:.2f}', end=' ')
for item in new_profit_prices:
    item = float(item)
    print(f'{item:.2f}', end=' ')
print()
print(f'Profit: {profit:.2f}')
if total_sum >= 150:
    print('Hello, France!')
else:
    print('Not enough money.')
