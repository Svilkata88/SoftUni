key = int(input())
n_lines = int(input())
decrypted_sentence = ''

for x in range(n_lines):
    letter = input()
    encrypted_letter = key + ord(letter)
    encrypted_letter_new = chr(encrypted_letter)
    decrypted_sentence += encrypted_letter_new

print(decrypted_sentence)


