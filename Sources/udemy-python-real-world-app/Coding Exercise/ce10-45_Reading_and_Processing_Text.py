# Reading and Processing Text (E)
# Read the bear.txt file, and print out the first 90 characters of its content.

# Hints: The file.read() method returns a string. You can use [:90] to extract the first 90 characters from that string. 
with open("bear.txt") as myfile:
    content = myfile.read()
    print(content[:90])

# Official Solution:
file = open("bear.txt")
content = file.read()
file.close()
print(content[:90])