string1 = input()
string2 = input()
output_string = None
new_output_string = string1

for i in range(len(string1)):
    new_string1 = string1[i+1:]
    new_string2 = string2[:i+1]
    output_string = new_string2 + new_string1
    if output_string != new_output_string:
        print(output_string)
        new_output_string = output_string



