# Integers are for representing whole numbers:
rank = 10
eggs = 12
people = 3

# Floats represent continuous value:
temperature = 10.2
rainfall = 5.98
elevation = 1031.88

# Strings represent any text:
message = "Welcome to our online shop!"
name = "John"
serial = "R001991981SW"

# Lists represent arrays of values that may change during the course of the program:
members = ["Sim Soony", "Marry Roundknee", "Jack Corridor"]
pixel_values = [252, 251, 251, 253, 250, 248, 247]

# Dictionaries represent pairs of keys and values:
phone_numbers = {"John Smith": "+37682929928", "Marry Simpons": "+423998200919"}
volcano_elevations = {"Glacier Peak": 3213.9, "Rainer": 4392.1}

# Keys of a dictionary can be extracted with:
phone_numbers.keys()
# Values of a dictionary can be extracted with:
phone_numbers.values()

# Tuples represent arrays of values that are not to be changed during the course of the program:
vowels = ('a', 'e', 'i', 'o', 'u')
one_digits = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

# To find out what attributes a type has:
dir(str)
dir(list)
dir(dict)

# To find out what Python builtin functions there are (type directly in Python interpreter):
# dir(__builtins__)

# Documentation for a Python command can be found with:
help(str)
help(str.replace)
help(dict.values)