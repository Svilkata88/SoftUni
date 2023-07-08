names = input().split(', ')

sorted_names = sorted(names, key=lambda x: (-len(x), x))
#sorted_names = [sorted_names[i] for i in range(len(sorted_names)-1,-1,-1)]

print(sorted_names)