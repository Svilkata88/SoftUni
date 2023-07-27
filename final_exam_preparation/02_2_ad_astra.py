import re

text_string = input()
day_calories = 2000
total_calories = 0

pattern = r'([\||#])([A-za-z\s]+)\1(\d{2}\/\d{2}\/\d{2})\1(\d{1,5})\1'

matches = re.findall(pattern, text_string)

for match in matches:
    total_calories += int(match[-1])
food_days = total_calories // day_calories

print(f'You have food to last you for: {food_days} days!')
for match in matches:
    print(f'Item: {match[1]}, Best before: {match[2]}, Nutrition: {match[3]}')
