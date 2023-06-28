n_snowballs = int(input())
highest_value = 0
max_weight = 0
max_time= 0
max_quality = 0

for ball in range(n_snowballs):
    weight_snowball = int(input())
    time_snowball = int(input())
    quality_snowball = int(input())

    snowball_value = (weight_snowball / time_snowball) ** quality_snowball
    if snowball_value > highest_value:
        highest_value = snowball_value
        max_weight = weight_snowball
        max_time = time_snowball
        max_quality = quality_snowball

print(f'{max_weight} : {max_time} = {int(highest_value)} ({max_quality})')

