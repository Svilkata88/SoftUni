number_of_electrons = int(input())
n = 1
shells_counter = []

while number_of_electrons > 0:
    shell_electrons_capacity = 2 * (n**2)
    if shell_electrons_capacity >= number_of_electrons:
        shells_counter.append(number_of_electrons)
        number_of_electrons = 0
    else:
        shells_counter.append(shell_electrons_capacity)
        number_of_electrons -= shell_electrons_capacity
    n += 1
print(shells_counter)