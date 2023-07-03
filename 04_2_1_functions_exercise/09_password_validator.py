def pass_validator(password):
    flag1 = False
    flag2 = False
    flag3 = False
    counter = 0
    if 5 < len(password) < 11:
        flag1 = True
    for ch in password:
        flag2 = True
        if ch.isalpha():
            flag2 = True
        if ch.isnumeric():
            flag2 = True
        else:
            flag2 = False
    for ch in password:
        if ch.isnumeric():
            counter += 1
        if counter >= 2:
            flag3 = True
    flag_list = [flag3, flag2, flag1]
    valid = [fl for fl in flag_list if fl]
    if len(valid) == 3:
        print('Password is valid')
    if len(valid) < 3:
        if not flag1:
            print('Password must be between 6 and 10 characters')
        if not flag2:
            print('Password must consist only of letters and digits')
        if not flag3:
            print('Password must have at least 2 digits')


password = input()
pass_validator(password)
