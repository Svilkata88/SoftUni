q_decorations = int(input())
days_to_christmas = int(input())
total_decoration = 0
total_christmas_spirit_points = 0

ORNAMENT_SET_PRICE = 2
THREE_SKIRT_PRICE = 5
THREE_GARLAND_PRICE = 3
THREE_LIGHT_PRICE = 15

ORNAMENT_SET_SPIRIT_POINTS = 5
THREE_SKIRT_SPIRIT_POINTS = 3
THREE_GARLAND_SPIRIT_POINTS = 10
THREE_LIGHT_SPIRIT_POINTS = 17

if days_to_christmas % 10 == 0:
    total_christmas_spirit_points -= 30

for days in range(1, days_to_christmas + 1):

    if days % 11 == 0:
        q_decorations += 2

    if days % 10 == 0:
        total_christmas_spirit_points -= 20
        total_decoration += THREE_SKIRT_PRICE + THREE_GARLAND_PRICE + THREE_LIGHT_PRICE

    if days % 5 == 0:
        total_decoration += q_decorations * THREE_LIGHT_PRICE
        total_christmas_spirit_points += THREE_LIGHT_SPIRIT_POINTS
        if days % 3 == 0:
            total_christmas_spirit_points += 30

    if days % 3 == 0:
        total_decoration += (THREE_SKIRT_PRICE + THREE_GARLAND_PRICE) * q_decorations
        total_christmas_spirit_points += THREE_SKIRT_SPIRIT_POINTS + THREE_GARLAND_SPIRIT_POINTS

    if days % 2 == 0:
        total_decoration += q_decorations * ORNAMENT_SET_PRICE
        total_christmas_spirit_points += ORNAMENT_SET_SPIRIT_POINTS

print(f'Total cost: {total_decoration}')
print(f'Total spirit: {total_christmas_spirit_points}')