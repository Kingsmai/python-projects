import os

# Know current working directory
print(os.getcwd())

# remove the file
os.unlink("data/origin/removethis.txt")

# remove this file if it is not empty, otherwise will throw an exception
os.rmdir("data/origin/removethisdir/")

import shutil
# if you want to remove the directory and its content
shutil.rmtree("data/origion/dirwithtree")
# this function will permanently delete and will not send to recycle bin


# Deleting can be dangerous so do a dry run first
# Dry Run
os.chdir("data/origin/")
for filename in os.listdir():
    if filename.endswith(".rxt"):
        print(filename)
        # os.unlink(filename) # Comment it before really delete it

# Using move2trash module (3rd party module) will help you to move file to the trash