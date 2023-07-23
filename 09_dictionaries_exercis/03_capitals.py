country_names = input().split(', ')
capital_names = input().split(', ')

names = {country_names[i]:capital_names[i] for i in range(len(country_names))}

for key, value in names.items():
    print(f'{key} -> {value}')
