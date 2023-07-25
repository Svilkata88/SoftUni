import re

text = input()
pattern = r'(\b(w{3})\.([A-Za-z0-9\-]+)(\.[a-z]+)+)'

while text:
    matches = re.findall(pattern, text)
    if matches:
        print(matches[0][0])

    text = input()