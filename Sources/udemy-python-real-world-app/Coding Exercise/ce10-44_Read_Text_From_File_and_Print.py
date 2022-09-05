# Read Text From File and Print (E)
# On the side panel there's a bear.txt file. The existing code opens that file in read mode.

# Below that code, please read the file content and print out the content.

# Hints: You can extract the content of a file with file.read().
file = open("bear.txt")
print(file.read())

# Official Solution:
file = open("bear.txt")
content = file.read()
print(content)