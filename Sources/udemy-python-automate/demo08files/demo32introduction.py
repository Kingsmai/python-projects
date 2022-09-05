# this is a simple file path, you need to use \\ to escape the \ symbol
_ = "c:\\spam\\eggs.png"

# Or you may use r"" as raw string
_ = r'c:\spam\eggs.png'

# If we have multiple folder, we can use list to contain the folder name and join them:
_ = "\\".join(["folder1", "folder2", "folder3", "file.png"])
# But this method work only on windows.

# Python give us os module
import os

# Then you can join the path using the os path module
os.path.join("folder1", "folder2", "folder3", "file.png")

# Current Working Directory tells the program what folder it should look in when we just handed a file name without file path
print(os.getcwd())

# We can change Current Working Directory with Change Directory function
os.chdir("c:\\")
print(os.getcwd())

# Change the cwd to our project directory
os.chdir("C:\\Users\\Xiaomai\\Desktop\\Python\\udemy-automate\\Sources")

# Get the absolute path of specific file
print(os.path.abspath("pe.txt"))
print(os.path.abspath("..\\notexist.txt"))
# This can be use to converting relative path into absolute path

# To check the path is absolute path, we can use:
print(os.path.isabs("..\\notexist.txt")) # this will return false since it is not a absolute path

# Get the relative path of absolute file
print(os.path.relpath("C:\\Windows\\System32\\cmd.exe", "C:\\Windows"))

# Just get the directory name
print(os.path.dirname("C:\\Windows\\System32\\cmd.exe"))

# Just get the file name
print(os.path.basename("C:\\Windows\\System32\\cmd.exe"))
# Also can use at folder name
print(os.path.basename("C:\\Windows\\System32"))

# Check the file is exist
print(os.path.exists("C:\\Windows\\System32\\cmd.exe"))
print(os.path.exists("../notexists.txt"))

# Check the path is a file
print(os.path.isfile("C:\\Windows\\System32\\cmd.exe"))

# Check the path is a directory
print(os.path.isdir("C:\\Windows\\System32"))

# Get the filesize
print(os.path.getsize("C:\\Windows\\System32\\cmd.exe"))

print(os.listdir("C:\\Windows\\System32"))

# Example finding the total size of all files in a folder
totalsize = 0

for filename in os.listdir("C:\\Windows\\System32"):
    if not os.path.isfile(os.path.join("C:\\Windows\\System32", filename)):
        continue
    totalsize = totalsize + os.path.getsize(os.path.join("C:\\Windows\\System32", filename))
print(totalsize)

os.makedirs("delicious\\icecream\\waffles")