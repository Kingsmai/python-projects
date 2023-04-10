encrypted_text = '-.-.-, --..-, -.--., --.., ----, -.-, ----, -..-'
encrypted_text = '----, -.-.-, --..-, -.--., --.., ----, -.-.., ----, -.-, ----, -..-'

if ',' in encrypted_text:
    encrypted_text_list = encrypted_text.split(', ')
else:
    encrypted_text_list = encrypted_text.split(' ')

# Convert morse code to binary
plain_list = []
for morse_code in encrypted_text_list:
    current_bin = ''
    for code in morse_code:
        if code == '-':
            current_bin += '1'
        else:
            current_bin += '0'
    # Convert to decimal
    decimal = int(current_bin, 2)
    # Convert to alphabet
    alphabet = chr(decimal + ord('a') - 1)
    plain_list.append(alphabet)

plain_list.reverse()
# separate into two line
mid = len(plain_list) // 2
if len(plain_list) % 2 != 0:
    mid += 1
separate_a = plain_list[:mid]
separate_b = plain_list[mid:]
print(separate_a)
print(separate_b)

plain_text = ''
for i in range(len(separate_a)):
    plain_text += separate_a[i]
    if i < len(separate_b):
        plain_text += separate_b[i]

print(plain_text)
