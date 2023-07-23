items = {'shards':0, 'fragments':0, 'motes':0}
obtained = False

while not obtained:
    entry_items = input().split()
    for index in range(0, len(entry_items), 2):
        value = entry_items[index]
        key = entry_items[index+1].lower()
        if key not in items:
            items[key] = 0
        items[key] += int(value)
        if items['shards'] >= 250:
            print('Shadowmourne obtained!')
            items['shards'] -= 250
            obtained = True
            break
        elif items['fragments'] >= 250:
            print('Valanyr obtained!')
            items['fragments'] -= 250
            obtained = True
            break
        elif items['motes'] >= 250:
            print('Dragonwrath obtained!')
            items['motes'] -= 250
            obtained = True
            break

print(f"shards: {items['shards']}\nfragments: {items['fragments']}\nmotes: {items['motes']}")
for key, value in items.items():
    if key != 'shards' and key != 'fragments' and key != 'motes':
        print(f'{key}: {value}')



