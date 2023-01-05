def morse_to_pinyin(morse_string):
    pinyin_dict = {
        ".-": "a",
        "-...": "b",
        "-.-.": "c",
        "-..": "d",
        ".": "e",
        "..-.": "f",
        "--.": "g",
        "....": "h",
        "..": "i",
        ".---": "j",
        "-.-": "k",
        ".-..": "l",
        "--": "m",
        "-.": "n",
        "---": "o",
        ".--.": "p",
        "--.-": "q",
        ".-.": "r",
        "...": "s",
        "-": "t",
        "..-": "u",
        "...-": "v",
        ".--": "w",
        "-..-": "x",
        "-.--": "y",
        "--..": "z"
    }
    pinyin_string = ""
    for word in morse_string.split("   "):
        for char in word.split(" "):
            pinyin_string += pinyin_dict[char]
        pinyin_string += " "
    return pinyin_string

morse_string = '... --- ...'

# 调用函数
pinyin_string = morse_to_pinyin(morse_string)
print(pinyin_string)