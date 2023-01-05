def binary_to_morse(binary_string):
    morse_string = ""
    for char in binary_string:
        if char == "0":
            morse_string += "."
        elif char == "1":
            morse_string += "-"
        else:
            morse_string += ' '
    return morse_string


def morse_to_text(morse_string):
    morse_code = {
        "A": ".-",        "B": "-...",
        "C": "-.-.",      "D": "-..",
        "E": ".",         "F": "..-.",
        "G": "--.",       "H": "....",
        "I": "..",        "J": ".---",
        "K": "-.-",       "L": ".-..",
        "M": "--",        "N": "-.",
        "O": "---",       "P": ".--.",
        "Q": "--.-",      "R": ".-.",
        "S": "...",       "T": "-",
        "U": "..-",       "V": "...-",
        "W": ".--",       "X": "-..-",
        "Y": "-.--",      "Z": "--..",
        "1": ".----",     "2": "..---",
        "3": "...--",     "4": "....-",
        "5": ".....",     "6": "-....",
        "7": "--...",     "8": "---..",
        "9": "----.",     "0": "-----"
    }
    text = ""
    for word in morse_string.split("   "):
        for char in word.split(" "):
            text += [key for key, value in morse_code.items() if value == char][0]
        text += " "
    return text


binary_string = '110 111 111 100'
morse_string = binary_to_morse(binary_string)
text = morse_to_text(morse_string)
print(text)

binary_string = '11 111 010 10 00 10 110'
morse_string = binary_to_morse(binary_string)
text = morse_to_text(morse_string)
print(text)

print('----------------------------')

binary_string = '011 100 10 11 100'
morse_string = binary_to_morse(binary_string)
text = morse_to_text(morse_string)
print(text)

binary_string = '011 1010 10 11'
morse_string = binary_to_morse(binary_string)
text = morse_to_text(morse_string)
print(text)

binary_string = '000 1000'
morse_string = binary_to_morse(binary_string)
text = morse_to_text(morse_string)
print(text)
