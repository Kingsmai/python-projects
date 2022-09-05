# Write First 90 (E)
# Create a first.txt file that contains the first 90 characters of bear.txt.

# Note that you should read the content of bear.txt with Python, extract its first 90 characters with Python, and write those characters in first.txt with Python.

# Hints: 
content = ''
with open("bear.txt") as bear:
    content = bear.read()
with open("first.txt", "w") as first:
    first.write(content[:90])