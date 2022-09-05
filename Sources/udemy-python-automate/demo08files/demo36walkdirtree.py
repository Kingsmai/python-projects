import os
import shutil

for folderName, subFolders, fileNames in os.walk("data/"):
    print("The folder is" + folderName)
    print("The subfolder in" + folderName + "are: " + str(subFolders))
    print("The filenames in" + folderName + "are: " + str(fileNames))
    print()

    for subFolder in subFolders:
        # Delete folder with this name
        if "fish" in subFolder:
            os.rmdir(subFolder)

    for file in fileNames:
        # backup all python source
        if file.endswith(".py"):
            shutil.copy(os.path.join(folderName, file), os.path.join(folderName, file + ".backup"))
