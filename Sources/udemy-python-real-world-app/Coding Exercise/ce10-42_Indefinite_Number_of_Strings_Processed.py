# Indefinite Number of Strings Processed (E)
# Define a function that takes an indefinite number of strings as parameters and returns a list containing all the strings in UPPERCASE and sorted alphabetically. For example, if I called your function with foo("snow", "glacier", "iceberg") it should return ["GLACIER", "ICEBERG", "SNOW"].

# Hints: Iterate through the list (or do list comrepehension) and apply str.upper() in each iteration. Also, good to know that the sorted(list) method returns a sorted list in alphabetical order. 
def foo(*args):
    return sorted([i.upper() for i in args])

# Official Solution:
def foo(*args):
    args = [x.upper() for x in args]
    return sorted(args)