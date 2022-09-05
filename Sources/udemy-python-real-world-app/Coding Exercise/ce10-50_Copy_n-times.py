# Copy n-times (E)
# The existing content of data.txt looks like this:

# 1.3, 1.5
# 2.3, 2.7
# Use Python to modify the content of data.txt so that its content looks like below:
# 1.3, 1.5
# 2.3, 2.7
# 1.3, 1.5
# 2.3, 2.7
# 1.3, 1.5
# 2.3, 2.7
# So, you need to find a way to insert the existing content two more times.

# Hints: Create a "with" block where you open the file in 'a+' mode. Put the cursor on top of the file. Read the file storing its content in a variable, put the cursor on top of the file, write the content, write the content.
with open("data.txt", "a+") as file:
    file.seek(0)
    content = file.read()
    for i in range(2):
        file.write(content)

# Official Solution:
with open("data.txt", "a+") as file:
    file.seek(0)
    content = file.read()
    file.seek(0)
    file.write(content)
    file.write(content)