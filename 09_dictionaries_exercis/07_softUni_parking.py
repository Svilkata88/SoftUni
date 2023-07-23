parking_data = {}
number_commands = int(input())

for _ in range(number_commands):
    input_string = input().split()

    if input_string[0] == 'register':
        command, username, car_plate = input_string[0], input_string[1], input_string[2]
        if username in parking_data:
            print(f'ERROR: already registered with plate number {car_plate}')
        else:
            parking_data[username] = car_plate
            print(f'{username} registered {car_plate} successfully')
    elif input_string[0] == 'unregister':
        command, username = input_string[0], input_string[1]
        if username not in parking_data:
            print(f'ERROR: user {username} not found')
        else:
            del parking_data[username]
            print(f'{username} unregistered successfully')

for k, v in parking_data.items():
    print(f'{k} => {v}')