import os, sys, time, transpositionEncrypt, transpositionDecrypt
from telnetlib import ENCRYPT

ENCRYPT = 'Encrypt'
DECRYPT = 'Decrypt'

def main():
    inputFileName = "Data/frankenstein.txt"
    # BE CAREFUL! If a file with the outputFileName name already exists
    # This program will overwrite that file:
    outputFileName = "Data/frankenstein.encrypted.txt"
    key = 10
    mode = ENCRYPT

    # If the input file does not exist the program terminates early:
    if not os.path.exists(inputFileName):
        print('The file %s does not exist. Quitting...' % (inputFileName))
        sys.exit()

    # If the output file already exist, give the user a chance to quit:
    if os.path.exists(outputFileName):
        print('This will overwrite the file %s. (C)ontinue or (Q)uit?' % (outputFileName))
        response = input('> ')
        if not response.lower().startswith('c'):
            sys.exit()

    # Read in the message from the input file
    fileObj = open(inputFileName)
    content = fileObj.read()
    fileObj.close()

    print('%sing...' % (mode.title()))

    # Measure how long the encryption / decryption takes:
    startTime = time.time()
    if mode == ENCRYPT:
        translated = transpositionEncrypt.encryptMessage(key, content)
    elif mode == DECRYPT:
        translated = transpositionDecrypt.decryptMessage(key, content)
    totalTime = round(time.time() - startTime, 2)
    print('%sion time: %s seconds' % (mode.title(), totalTime))

    # Write out the translated message to the output file
    outputFileObj = open(outputFileName, 'w')
    outputFileObj.write(translated)
    outputFileObj.close()

    print('Done %sing %s (%s characters).' % (mode, inputFileName, len(content)))
    print('%sed file is %s' % (mode.title(), outputFileName))


if __name__ == "__main__":
    main()