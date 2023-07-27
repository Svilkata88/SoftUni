def add(piece, composer, key):
    if piece not in pieces_data:
        pieces_data[piece] = [composer, key]
        print(f'{piece} by {composer} in {key} added to the collection!')
    else:
        print(f'{piece} is already in the collection!')


def remove(piece):
    if piece in pieces_data:
        del pieces_data[piece]
        print(f'Successfully removed {piece}!')
    else:
        print(f'Invalid operation! {piece} does not exist in the collection.')


def change_key(piece, new_key):
    if piece in pieces_data:
        pieces_data[piece][1] = new_key
        print(f'Changed the key of {piece} to {new_key}!')
    else:
        print(f'Invalid operation! {piece} does not exist in the collection.')


n_pieces = int(input())
pieces_data = {}

for _ in range(n_pieces):
    pieces = input().split('|')
    piece, composer, key = pieces
    if piece not in pieces_data:
        pieces_data[piece] = [composer, key]

commands = input().split('|')

while commands[0] != 'Stop':
    command, *others = commands
    if command == 'Add':
        piece, composer, key = others
        add(piece, composer, key)

    elif command == 'Remove':
        piece = others[0]
        remove(piece)

    elif command == 'ChangeKey':
        piece, new_key = others
        change_key(piece, new_key)

    commands = input().split('|')

for k, v in pieces_data.items():
    print(f'{k} -> Composer: {v[0]}, Key: {v[1]}')