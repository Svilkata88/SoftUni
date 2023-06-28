num = int(input())
list_sums = 0
list_elements = []

for n in range(1, num+1):
    for i in str(n):
        list_sums += int(i)
    if list_sums == 5 or list_sums == 7 or list_sums == 11:
        print(n, '-> True')
    else:
        print(n, '-> False')
    list_sums = 0