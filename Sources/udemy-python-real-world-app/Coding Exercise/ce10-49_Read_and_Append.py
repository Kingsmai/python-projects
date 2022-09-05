# Read and Append (E)
# Append the text of bear1.txt to bear2.txt. In other words, bear2.txt should contain its text and the text of bear1.txt after that.

# Hints: Use two separate "with" blocks. In the first "with" block, open bear1.txt in 'r' mode and store its text in a variable. In the second "with" block, open bear2.txt in 'a' mode, and write the text of bear1.txt in that file.
with open("bear1.txt") as bear:
    content = bear.read()

with open("bear2.txt", "a") as bear:
    bear.write(content)