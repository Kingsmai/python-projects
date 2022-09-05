# Write Snail (E)
# Use Python to create a file with name file.txt and write the text snail there.

# Hints: Open a 'file.txt' in 'w' mode using the with context manager and under 'with' use a write('snail') method.
with open("file.txt", "w") as myfile:
    myfile.write("snail")