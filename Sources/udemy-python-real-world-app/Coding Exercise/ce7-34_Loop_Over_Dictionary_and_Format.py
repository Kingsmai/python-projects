# Loop Over Dictionary and Format (E)
# Make the code print out the following output using a for loop:

# John Smith: +37682929928
# Marry Simpons: +423998200919

# So, the code should loop over the dictionary items and in each iteration should print out the dictionary key, a colon, a space, and the corresponding  value.

# Hints: You can iterate over a dictionary with:
# for key, value in phone_numbers.items():
# Then, in the loop, use string formatting to build a string that accesses values from the key and value variables.
phone_numbers = {"John Smith": "+37682929928", "Marry Simpons": "+423998200919"}

for key, value in phone_numbers.items():
    print("{}: {}".format(key, value))

# Official Solution:
phone_numbers = {"John Smith": "+37682929928", "Marry Simpons": "+423998200919"}

for key, value in phone_numbers.items():
    print("%s: %s" % (key, value))