# CaesarCipher

# I copy this SYMBOLS from another file
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.`~@#$%^&*()_+-=[]{}|;:",<>/'

message = input("Enter your message: ")

# Get key
while True:  # Keep looping until user input a valid key
    key = input("Enter your key, keys must between (1 ~ " + str(len(SYMBOLS)) + "): ")
    if (key.isdigit() and 0 < int(key) <= len(SYMBOLS)):
        key = int(key)
        break
    else:
        print("The key is invalid, please try again.\n")
        
# Get mode
while True:
    mode = input("Please select your mode (E)ncrypt / (D)ecrypt: ").upper()
    if (mode.startswith('E') or mode.startswith('D')):
        break
    else:
        print("Invalid input, please try again")

translated = ''

for character in message:
    if character in SYMBOLS:
        symbolIndex = SYMBOLS.find(character)

        if mode.startswith('E'): # Encrypt
            translatedIndex = symbolIndex + key
        elif mode.startswith('D'): # Decrypt
            translatedIndex = symbolIndex - key

        # Handle wraparound
        if translatedIndex >= len(SYMBOLS):
            translatedIndex -= len(SYMBOLS)
        elif translatedIndex < 0:
            translatedIndex += len(SYMBOLS)

        translated += SYMBOLS[translatedIndex]
    else:
        translated += character

print(translated)
