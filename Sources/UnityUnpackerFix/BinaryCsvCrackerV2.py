bin_filepath = r'C:\Users\xsbug\OneDrive\Desktop\SK503\Assets\Resources\soulknight\runtime\config2code\encryptedcsv' \
                 r'\enemies.bytes'
                 # r'\skills.bytes'
save_filepath = r'C:\Users\xsbug\Nox_share\ImageShare\game.data'


def xor_crypt_string(data, key='soulKnight', encode=False, decode=False):
    print()
    print(key * 3)
    from itertools import cycle
    import base64
    if decode:
        data = str(base64.b64decode(data))[2:-1]
    xored = ''.join(chr(ord(x) ^ ord(y)) for (x, y) in zip(data, cycle(key)))
    if encode:
        return base64.encodestring(xored).strip()
    return xored


bin_file = open(bin_filepath, 'r')
ciphertext = ''.join(bin_file.readlines())
bin_file.close()

decrypted = xor_crypt_string(ciphertext)
print(decrypted)

output_filepath = r"C:\Users\xsbug\OneDrive\Desktop\enemy.csv"
output_file = open(output_filepath, 'w')
output_file.writelines(decrypted)
output_file.close()
