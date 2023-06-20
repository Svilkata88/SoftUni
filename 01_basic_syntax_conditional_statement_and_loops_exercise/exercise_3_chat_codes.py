n_messages = int(input())

for x in range(n_messages):
    numbers = int(input())
    if numbers == 88:
        print('Hello')
    elif numbers == 86:
        print('How are you?')
    elif numbers < 88:
            print('GREAT!')
    elif numbers > 88:
        print('Bye.')


