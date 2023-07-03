def rounding(string):
    string = string.split()
    string_rounded = [round(float(ch)) for ch in string]
    return string_rounded

string = input()
print(rounding(string))