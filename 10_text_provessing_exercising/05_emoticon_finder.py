text = input()

for i,ch in enumerate(text):
    if ch == ':':
        print(f'{ch}{text[i+1]}')