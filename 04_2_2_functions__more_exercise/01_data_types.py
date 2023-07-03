def data_types():
    data_type_input = input()
    num1 = input()
    result = 0
    if data_type_input == 'int':
        result = int(num1) * 2
    elif data_type_input == 'real':
        result = float(num1) * 1.5
        result = f'{result:.2f}'
    elif data_type_input == 'string':
        result = f'${num1}$'
    return result


print(data_types())
