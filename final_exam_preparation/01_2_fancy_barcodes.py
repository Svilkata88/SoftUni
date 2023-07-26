import re

number_inputs = int(input())

pattern_barcode = r'(@#+([A-Z][A-Za-z\d]{4,}[A-Z])@#+)'

for _ in range(number_inputs):
    barcodes = input()
    matches = re.findall(pattern_barcode, barcodes)
    if matches:
        digits = ''
        barcode_text = matches[0][1]
        for ch in barcode_text:
            if ch.isdigit():
                digits += ch
        if digits == '':
            print(f'Product group: 00')
        else:
            print(f'Product group: {digits}')
    else:
        print('Invalid barcode')