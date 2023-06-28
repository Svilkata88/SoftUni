numbers = input()
new_list = [int(el) for el in numbers.split(', ')]

for index, items in enumerate(new_list):
    if items == 0:
        new_list.remove(items)
        new_list.append(items)

print(new_list)