budget = float(input())
kg_flour_price = float(input())
eggs_count = 0

pack_of_eggs_price = kg_flour_price * 0.75
liter_of_milk_price = kg_flour_price * 1.25
milk_needed_price = liter_of_milk_price / 4

one_loaf_price = pack_of_eggs_price + kg_flour_price + milk_needed_price

number_loaves = budget // one_loaf_price
total_loaves_price = number_loaves * one_loaf_price
budget_left = budget - total_loaves_price

for i in range(1, int(number_loaves) + 1):
    eggs_count += 3
    if i % 3 == 0:
        eggs_count -= i - 2

print(f'You made {int(number_loaves)} loaves of Easter bread! Now you have {int(eggs_count)}'
      f' eggs and {budget_left:.2f}BGN left.')
