#Sometimes you might need to convert between different data types in Python for one reason or another. That is very easy to do:

# From tuple to list:
data = (1, 2, 3)
print(list(data))

# From list to tuple:
data = [1, 2, 3]
tuple(data)

# From list to dictionary:
data = [["name", "John"], ["surname", "smith"]]
dict(data)

# Note that the original data type needs to have the data structured in a way that can be understood by the new data type.
# For example, the following would not work:
data = [1, 2, 3]
# dict(data) # TypeError: cannot convert dictionary update sequence element #0 to a sequence
# That's because a dictionary is made of key and value pairs, but the list was not constructed that way, so the above would generate an error.