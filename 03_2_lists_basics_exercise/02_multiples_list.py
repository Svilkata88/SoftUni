factor = int(input())
count = int(input())
multiples = []
new_factor = factor

while len(multiples) < count:
    if new_factor % factor == 0:
        multiples.append(new_factor)

    new_factor += 1

print(multiples)

