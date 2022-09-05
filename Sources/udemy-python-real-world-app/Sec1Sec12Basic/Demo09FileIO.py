# import os


# print(os.getcwd())
myfile = open("fruits.txt") # open method will put the "cursor" at the beginning of the file
content = myfile.read() # read method will iterate the "cursor" to the end of file, and get the whole file content
# So when we use read method twice, it will read nothing because the "cursor" is at the end of the file
# after operate the file, you need to close it to remove it from your RAM
myfile.close()

print(content) # you can still print the content even the file is closed

# Opening file using "with"
with open("fruits.txt") as myfile:
    content = myfile.read()
# you don't need to close file manually

# Filepaths
# you need to type the complete filepath to find the file
with open("files/cars.txt") as myfile:
    content = myfile.read()

print(content)


# Writing text to a file
# open got parameter 'mode' of opening file. Default is "r" means "read"
# create a "vegetables.txt" in "files" folder
# mode='w' means "write" it will create the file if it doesn't exist;
# ! But! If the file is exists, Python will overwrite the old with the brand new text
with open("files/vegetables.txt", mode='w') as myfile:
    myfile.write("Tomato\nCucumber\nOnion\n") # Write text in the vegetables.txt
    # use \n to write more lines
    # You may write more lines of write method, which will append the file continuously
    myfile.write("Garlic\n") # Remember to add \n after the last line since the text will append behind the last line

# Appending Text to an Existing File:
# 'a' stand for append, it won't overwrite the existing file.
# '+' open a disk file for updating (reading and writing)
with open("files/vegetables.txt", "a+") as myfile:
    myfile.write("Carrot\n") # When we write "Carrot", the cursor will stop at the End of the file
    myfile.seek(0) # put the cursor back to the start of the file
    content = myfile.read()
    print(content)