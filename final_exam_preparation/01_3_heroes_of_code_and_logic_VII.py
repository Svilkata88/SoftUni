def cast_spell(hero, MP_needed, spell_name):
    if heroes[hero][1] >= MP_needed:
        heroes[hero][1] -= MP_needed
        return f'{hero} has successfully cast {spell_name} and now has {heroes[hero][1]} MP!'
    return f'{hero} does not have enough MP to cast {spell_name}!'


def take_dmg(hero, dmg, attacker):
    if heroes[hero][0] > dmg:
        heroes[hero][0] -= dmg
        return f'{hero} was hit for {dmg} HP by {attacker} and now has {heroes[hero][0]} HP left!'
    else:
        del heroes[hero]
        return f'{hero} has been killed by {attacker}!'


def recharge(hero, mana_points_recharged):
    if mana_points_recharged + heroes[hero][1] >= 200:
        amount_recovered = 200 - heroes[hero][1]
        heroes[hero][1] = 200
    else:
        heroes[hero][1] += mana_points_recharged
        amount_recovered = mana_points_recharged
    return f'{hero} recharged for {amount_recovered} MP!'


def heal(hero, hp_recharged):
    if hp_recharged + heroes[hero][0] >= 100:
        amount_recovered = 100 - heroes[hero][0]
        heroes[hero][0] = 100
    else:
        heroes[hero][0] += hp_recharged
        amount_recovered = hp_recharged
    return f'{hero} healed for {amount_recovered} HP!'


n = int(input())
heroes = {}

for _ in range(n): # creating heroes dict.
    input_hero = input()
    hero_name, HP, MP = input_hero.split()
    heroes[hero_name] = [int(HP), int(MP)]

command = input()
while command != 'End': # starting the game!
    action, *others = command.split(' - ')
    if action == 'CastSpell':
        hero, mana_points, spell_name = others
        mana_points = int(mana_points)
        print(cast_spell(hero, mana_points, spell_name))

    elif action == 'TakeDamage':
        hero, dmg, attacker = others
        dmg = int(dmg)
        print(take_dmg(hero, dmg, attacker))

    elif action == 'Recharge':
        hero, mana_points_recharged = others
        mana_points_recharged = int(mana_points_recharged)
        print(recharge(hero, mana_points_recharged))

    elif action == 'Heal':
        hero, hp_recharged = others
        hp_recharged = int(hp_recharged)
        print(heal(hero, hp_recharged))

    command = input()

for heroes_members, values in heroes.items():
    print(heroes_members)
    print(f'  HP: {values[0]}')
    print(f'  MP: {values[1]}')