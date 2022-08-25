import math

def main():
    secretMessage = "Cenoonommstmme oo snnio s s c"
    secretKey = 8

    plaintext = decryptMessage(secretKey, secretMessage)

    # Print with a | ("pipe" character) after it in case
    # there are spaces at the end of the decrypted message:
    print(plaintext + '|')

def decryptMessage(key, message):
    # The transposition decrypt function will simulate the "columns" and
    # "rows" of the grid that the plaintext is written on by using a list
    # of strings. First, we need to calculate a few values.

    # The number of "columns" in our transposition grid:
    numOfColumns = int(math.ceil(len(message) / float(key)))
    # The number of "rows" in our transposition grid:
    numOfRows = key
    # The number of "shaded boxes" in the last "column" of the grid:
    numOfShadedBoxes = (numOfColumns * numOfRows) - len(message)

    # Each string in plaintext represents a column in the grid:
    plaintext = [""] * numOfColumns

    # The column and row variables point to where in the grid the next
    # character in the encrypted message will go:
    column = 0
    row = 0

    for symbol in message:
        plaintext[column] += symbol
        column += 1

        # If there are no more columns OR ve're at a shaded box, go back
        # to the first column and the next row:
        if (column == numOfColumns) or (column == numOfColumns - 1 and row >= numOfRows - numOfShadedBoxes):
            column = 0
            row += 1

    return ''.join(plaintext)


if __name__ == "__main__":
    main()