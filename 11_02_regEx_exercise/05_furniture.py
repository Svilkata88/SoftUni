import re

purchase = input()
pattern = r'>>([A-za-z]+)<<(\d+\.?\d*)!(\d+)'
purchases = []
total_costs = 0
while purchase != 'Purchase':
    result = re.search(pattern, purchase)
    if result:
        purchases.append(result.group(1))
        price = result.group(2)
        quantity = result.group(3)
        total_costs += float(price) * int(quantity)
    purchase = input()

print('Bought furniture:')
for purchase in purchases:
    print(purchase)
print(f'Total money spend: {total_costs:.2f}')