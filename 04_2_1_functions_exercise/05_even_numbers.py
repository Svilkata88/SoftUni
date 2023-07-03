def even_numbers(ch):
    if ch % 2 == 0 and ch != 0:
        return ch


string = input().split()
int_string = [int(ch) for ch in string]
int_string = [num for num in int_string if num % 2 == 0]
#result = list(filter(even_numbers, int_string))
print(int_string)