num1 = input().split()
num2 = input().split()
num3 = input().split()
tp = []
win_list = []

game_list = num1 + num2 + num3
game_list = [int(ch) for ch in game_list]

win_column_1 = [1, 4, 7]
win_column_2 = [2, 5, 8]
win_column_3 = [3, 6, 9]
win_row_1 = [1, 2, 3]
win_row_2 = [4, 5, 6]
win_row_3 = [7, 8, 9]
diagonal_1 = [1, 5, 9]
diagonal_2 = [3, 5, 7]
elements = [win_column_1, win_column_2, win_column_3, win_row_1, win_row_2, win_row_3, diagonal_1, diagonal_2]

for element in elements:
    for num in range(1, len(game_list) + 1):
        if num in element:
            tp.append(game_list[num - 1])

    if tp[0] == tp[1] == tp[2]:
        if 1 in tp:
            print('First player won')
            break
        elif 2 in tp:
            print('Second player won')
            break
        else:
            tp = []
    else:
        tp = []
if len(tp) == 0:
    print('Draw!')

