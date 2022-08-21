def main():
    message = 'Common sense is not so common'
    key = 8

    ciphertext = encryptMessage(key, message)

    # Print the encrypted string in ciphertext to the screen, with
    # a | ("pipe" character) after it in case thete are spaces at
    # the end of the encrypted message:
    print(ciphertext + '|')

def encryptMessage(key, message):
    # Each string in ciphertext represents a column in the grid:
    ciphertext = [''] * key

    # Loop through each column in ciphertext:
    for column in range(key):
        currentIndex = column

        # Keep looping until currentIndex goes past the message length:
        while currentIndex < len(message):
            # Place the character at currentIndex in message at the
            # end of the current column in the ciphertext list:
            ciphertext[column] += message[currentIndex]

            # Move the currentIndex over:
            currentIndex += key

    # Convert the ciphertext list into a single string value and return it:
    return "".join(ciphertext)

# If transpositionEncrpyt.py is run (instead of imported as a module) call
# The main() function:
if __name__ == "__main__":
    main()