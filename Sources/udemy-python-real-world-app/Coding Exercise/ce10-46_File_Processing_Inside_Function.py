# File Processing Inside Function (E)
# Define a function that gets a single string character and a filepath as parameters and returns the number of occurences of that character in the file.

# Hints: Define the function with:
# def(character, filepath)
# Load its content in a string and then use the str.count(character) method.
def foo(character, filepath="bear.txt"):
    count = 0
    with open(filepath) as myfile:
        content = myfile.read()
        for i in content:
            if i == character:
                count += 1
        return count

# Official Solution:
def foo(character, filepath="bear.txt"):
    file = open(filepath)
    content = file.read()
    return content.count(character)