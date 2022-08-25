# Reverse Cipher by Xiaomai
message = input("Enter the message here: ")
i = len(message)
translate = ''
while i > 0:
    translate += message[i - 1]
    i -= 1
print(translate)