def abjuration():
    new_string = spell.upper()
    return new_string


def necromancy():
    new_string = spell.lower()
    return new_string


def deviation(substring, replacement):
    new_string = spell.replace(substring, replacement)
    return new_string

def illusion(index, letter):
    if index in range(0, len(spell)):
        cutted_part = spell[index:index+1]
        new_string = spell.replace(cutted_part, letter, 1)
        print(f'Done!')
        return new_string
    else:
        print(f'The spell was too weak.')
        return spell


def alteration(substring):
    new_string = spell.replace(substring, '', 1)
    return new_string


spell = input()

commands = input()
while commands != 'Abracadabra':
    command, *others = commands.split()
    if command == 'Abjuration':
        print(abjuration())
        spell = abjuration()
    elif command == 'Necromancy':
        print(necromancy())
        spell = necromancy()
    elif command == 'Illusion':
        index, letter = others
        index = int(index)
        spell = illusion(index, letter)
    elif command == 'Divination':
        substring, replacement = others
        if substring in spell:
            spell = deviation(substring, replacement)
            print(spell)
        else:
            break
    elif command == 'Alteration':
        substring = others[0]
        if substring in spell:
            spell = alteration(substring)
            print(spell)
        else:
            break
    else:
        print('The spell did not work!')

    commands = input()