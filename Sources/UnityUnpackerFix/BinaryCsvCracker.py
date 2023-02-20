bin_filepath_1 = r'C:\Users\xsbug\OneDrive\Desktop\SK503\Assets\Resources\soulknight\runtime\config2code\encryptedcsv' \
                 r'\mounts.bytes'

bin_filepath_2 = r'C:\Users\xsbug\OneDrive\Desktop\SK503\Assets\Resources\soulknight\runtime\config2code\encryptedcsv' \
                 r'\pets.bytes'

# ========================
# FAILED!!!
# ========================

bin_file = open(bin_filepath_2, 'rb')

binary = ''
hexadecimal = ''

for line in bin_file:
    for char in line:
        binary += bin(char)[2:]
        hexadecimal += hex(char)[2:]

print(binary)
print(hexadecimal)

# 遍历 binary
byte_len = 8
for i in range(0, len(binary), byte_len):
    byte = binary[i: i + byte_len]
    num = int(byte, 2)
    print(chr(num), end='')

# 遍历 hex
byte_len = 2
for i in range(0, len(hexadecimal), byte_len):
    byte = hexadecimal[i: i + byte_len]
    num = int(byte, 16)
    print(chr(num), end='')

bin_file.close()
