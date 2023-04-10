plain_text = 'iloveyoutoo'

# Separate text into two string with 13579 2468...
separate_a = ''
separate_b = ''

for idx, ch in enumerate(plain_text):
    if idx % 2 == 0:
        separate_a += ch
    else:
        separate_b += ch

# Combine the separated text and reverse it
crypt_text = separate_a + separate_b
crypt_text = crypt_text[::-1].lower()

# convert the alphabets into numbers
alpha_num = []
for ch in crypt_text:
    alpha_num.append(ord(ch) - ord('a') + 1)

# convert the alpha_num to binary
num_bin = []
for num in alpha_num:
    num_bin.append(bin(num)[2:])

# convert the num to morse like code
encrypted_text = []
for bin_str in num_bin:
    current_str = ''
    for bin_num in bin_str:
        if bin_num == '1':
            current_str += '-'
        else:
            current_str += '.'
    encrypted_text.append(current_str)

result_text = ', '.join(encrypted_text)
print(result_text)
