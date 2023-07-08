def add_Book(string, book_name):
    if book_name not in string:
        string.insert(0, book_name)
    return string


def take_book(string, book_name):
    if book_name in string:
        string.remove(book_name)
    return string


def swap_book(string, book1, book2):
    if book1 and book2 in string:
        b1 = string.index(book1)
        b2 = string.index(book2)
        string[b1], string[b2] = string[b2], string[b1]
    return string


def insert_book(string, book_name):
    if book_name not in string:
        string.append(book_name)
    return string


def check_book(string, index):
    return string[index]


string = input().split('&')

while True:
    command = input().split(' | ')
    if command[0] == 'Done':
        break
    if command[0] == 'Add Book':
        add_Book(string, command[1])
    elif command[0] == 'Take Book':
        take_book(string, command[1])
    elif command[0] == 'Swap Books':
        swap_book(string, command[1], command[2])
    elif command[0] == 'Insert Book':
        insert_book(string, command[1])
    elif command[0] == 'Check Book':
        print(check_book(string, int(command[1])))



print(', '.join(string))

