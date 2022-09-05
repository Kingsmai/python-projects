import shutil # let us copy move rename and delete files

# Copy a file to destination folder
shutil.copy("data/origin/test.txt", "data/dest/")

# Copy a file to destination folder and rename it
shutil.copy("data/origin/test.txt", "data/dest/testspam.txt")

# Copy entire folder
shutil.copytree("data/origin/testdir", "data/dest/testdirbackup")

# Move a file
shutil.move("data/origin/testmove.txt", "data/dest/")

# Rename a file
shutil.move("data/origin/spam.txt", "data/origin/rename.txt")