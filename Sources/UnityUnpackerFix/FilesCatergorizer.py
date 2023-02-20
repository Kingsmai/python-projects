import os
import re
import shutil

filepath = r"C:\Users\xsbug\OneDrive\Desktop\SK503 Resource\Images"
searchkeyword = 'ui'
filenamepattern = searchkeyword + r'\d?[^a-z]'
outputpath = os.path.join(filepath, searchkeyword)

if not os.path.exists(outputpath):
    os.mkdir(outputpath)

for filename in os.listdir(filepath):
    orifilepath = os.path.join(filepath, filename)
    if os.path.isdir(orifilepath):
        print(orifilepath)
        continue
    if re.search(filenamepattern, filename):
        print(filename)
        destfilepath = os.path.join(outputpath, filename)
        shutil.copy(orifilepath, destfilepath)
