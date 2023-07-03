def sorted_list(numbers):
    numbers = [int(ch) for ch in numbers]
    numbers.sort()
    return numbers


numbers = input().split()
print(sorted_list(numbers))
