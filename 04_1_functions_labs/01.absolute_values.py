def absolute_values_list (sentence_of_numbers):
    sentence_of_numbers = sentence_of_numbers.split()
    sentence_of_numbers = [abs(float(ch)) for ch in sentence_of_numbers]
    return sentence_of_numbers


sentence_of_numbers = input()
print(absolute_values_list(sentence_of_numbers))

