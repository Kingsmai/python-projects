"""
练习内容：在密码学中，恺撒密码（英语：Caesar cipher），或称恺撒加密、恺撒变换、变换加密，是一种最简单且最广为人知的加密技术。
它是一种替换加密的技术，明文中的所有字母都在字母表上向后（或向前）按照一个固定数目进行偏移后被替换成密文。
例如，当偏移量是3的时候，所有的字母A将被替换成D，B变成E，以此类推。
这个加密方法是以罗马共和时期恺撒的名字命名的，当年恺撒曾用此方法与其将军们进行联系。
请使用键盘输入偏移量，并使用偏移量对键盘输入对单个大写英文字母进行加密。
如偏移量为3，输入英文字母为Z，则输出为C。
"""


def caesar_cipher(plaintext: str, offset: int) -> str:
    result = ""
    for char in plaintext:
        if char.isalpha():
            shifted_char = chr((ord(char) - 65 + offset) % 26 + 65) if char.isupper() else chr(
                (ord(char) - 97 + offset) % 26 + 97)
            result += shifted_char
        else:
            result += char  # 非字母保持原样
    return result


plain = "Hello, world!, zombie!!"
caesar_cipher(plain, 3)
