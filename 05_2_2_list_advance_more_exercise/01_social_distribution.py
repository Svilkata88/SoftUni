population = input().split(', ')
minimum_wealth = int(input())
condition = False

population = [int(num) for num in population]
for i in range(len(population)):

    if population[i] < minimum_wealth:
        diff = minimum_wealth - int(population[i])
        population[i] += diff
        biggest = max(population)
        biggest -= diff
        population[population.index(max(population))] = biggest
    if population.count(min(population)) > 2:
        condition = True

if condition:
    print(population)
else:
    print('No equal distribution possible')

