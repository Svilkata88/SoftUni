year = int(input())

while True:
    year += 1
    num_set = set(str(year))
    if len(list(num_set)) == len(str(year)):
        print(year)
        break
    else:
        continue
