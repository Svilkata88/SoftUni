
def merge(string_list, start_index, end_index):
    if end_index > len(string_list)-1:
        end_index = len(string_list)
    merged_strings = [string_list[i] for i in range(len(string_list)) if i in range(start_index, end_index+1)]
    merged_strings = ''.join(merged_strings)
    string_list = list(string_list)
    while end_index >= start_index:
        end_index -= 1
        if len(string_list) == start_index:
            break
        string_list.pop(start_index) if end_index != 0 else string_list.pop(start_index)
    string_list.insert(start_index, merged_strings)

    return string_list


def divide(strings_list, index, pieces):
    for i in range(len(strings_list)):
        if i == index:
            word = strings_list[index]
            strings_list.pop(index)
            break
    if len(word) < pieces:
        one_equal_piece_length = 1
    else:
        one_equal_piece_length = len(word) // pieces
    last_part_piece = len(word) % pieces + one_equal_piece_length
    word_list = list(word)
    divided_words = []
    for i in range(pieces):
        word_piece = []
        if i == pieces - 1:
            word_piece = [''.join(word_list)]
            word_piece = ''.join(word_piece)
            divided_words.append(word_piece)
            break
        for index_part in range(one_equal_piece_length):
            word_piece.append(word_list[index_part])
            if len(word_list) == last_part_piece:
                word_piece = [''.join(word_list)]
        for index_part in range(one_equal_piece_length):
            if len(word_list) == last_part_piece:
                word_list = []
                break
            word_list.pop(0)
        word_piece = ''.join(word_piece)
        divided_words.append(word_piece)

    [strings_list.insert(index, divided_words[i]) for i in range(len(divided_words) - 1, -1, -1)]

    return strings_list


strings_list = input().split()
while True:
    command = input().split()
    if command[0] == '3:1':
        break
    if command[0] == 'merge':
        strings_list = merge(strings_list, int(command[1]), int(command[2]))
    elif command[0] == 'divide':
        strings_list = divide(strings_list, int(command[1]), int(command[2]))

print(' '.join(strings_list))

