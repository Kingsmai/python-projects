secretMessage = input("Please input the message you want to decrypt: ")

SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.`~@#$%^&*()_+-=[]{}|;:",<>/'


for key in range(len(SYMBOLS)):
    plainText = ''
    for character in secretMessage:
        if character in SYMBOLS:
            symbolIndex = SYMBOLS.find(character)
            plainIndex = symbolIndex - key
            if plainIndex >= len(SYMBOLS):
                plainIndex -= len(SYMBOLS)
            elif plainIndex < 0:
                plainIndex += len(SYMBOLS)
            plainText += SYMBOLS[plainIndex]
        else:
            plainText += character
    print("Key #" + str(key) + ": " + plainText)