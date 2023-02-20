import itertools

bin_filepath = r'C:\Users\xsbug\OneDrive\Desktop\SK503\Assets\Resources\soulknight\runtime\config2code\encryptedcsv' \
                 r'\mounts.bytes'

bin_file = open(bin_filepath, 'r')
cipherText = bin_file.readlines()
print(cipherText)
bin_file.close()


def decrypt(cipher_text: str, password: str):
    length = len(cipher_text)
    for i in range(length):
        cipher_text = (cipher_text[:i] + chr(ord(cipher_text[i]) * ord(password)) + cipher_text[i + 1:])
        print(cipher_text[i], end='')


decrypt(cipherText[2], '9')

# POSSIBLE_CHARACTER = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890~`!@#$%^&*()_-+={[}]|\\:;\"'<,>.?/"
#
# passwords = [''.join(letters)
#              for length in range(1, 20)
#              for letters in itertools.product(POSSIBLE_CHARACTER, repeat=length)]
#
# for pwd in passwords:
#     pass


