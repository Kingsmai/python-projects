# Loop Over Dictionary and Replace (E)
# Loop over the phone_numbers values and in each loop print out the phone number, but with '00' instead of '+'. In other words, your code should output:

# 0037682929928
# 00423998200919

# Hints: You could make use of the str.replace(char1, char2) method for this. It replaces char1 with char2 in the string.
phone_numbers = {"John Smith": "+37682929928", "Marry Simpons": "+423998200919"}

for number in phone_numbers.values():
    print("00" + number[1:])

# Official Solution:
phone_numbers = {"John Smith": "+37682929928", "Marry Simpons": "+423998200919"}

for value in phone_numbers.values():
    print(value.replace("+", "00"))