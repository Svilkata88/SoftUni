lost_fights_count = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

broken_helmet = 0
broken_sword = 0
broken_shield = 0
broken_armor = 0
expenses = 0

for lost_game in range(1, lost_fights_count + 1):
    if lost_game > 0:
        if lost_game % 2 == 0:
            broken_helmet += 1
        if lost_game % 3 == 0:
            broken_sword += 1
        if lost_game % (3 * 2) == 0:
            broken_shield += 1
        if lost_game % (6 * 2) == 0:
            broken_armor += 1
        expenses = helmet_price * broken_helmet + sword_price * broken_sword + shield_price * broken_shield \
                   + armor_price * broken_armor
    else:
        print(f'Gladiator expenses: {0:.2f} aureus')
print(f'Gladiator expenses: {expenses:.2f} aureus')
