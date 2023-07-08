to_do_list = []

while True:
    note = input()
    if note == 'End':
        break
    to_do_list.insert(0, note)

sorted_to_do_list = sorted(to_do_list, key=lambda x: int(x.split('-')[0]))
sorted_to_do_list = [word.split('-')[1] for word in sorted_to_do_list]

print(sorted_to_do_list)
