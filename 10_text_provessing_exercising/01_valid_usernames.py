def length_validation(user):
    if 3 <= len(user) <= 16:
        return True
    return False


def char_validation(user):
    for ch in user:
        if not ch.isalnum() and (not ch == '-') and (not ch == '_'):
            return False
    return True


def redundant_symbols_validation(user):
    if ' ' in user:
        return False
    return True


def is_valid(username):
    if length_validation(username) and char_validation(username) and redundant_symbols_validation(username):
        return True
    return False


usernames = input().split(', ')
for user in usernames:
    if is_valid(user):
        print(user)