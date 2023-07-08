string = input()

vowels = ['a', 'o', 'u', 'e', 'i']
output = [ch for ch in string if ch.lower() not in vowels]
output_string = ''.join(output)

print(output_string)