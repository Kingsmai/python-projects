# Use pip to install third party module
# usage pip install <module-name>

import time # Built-in library
import os # Standard library
import pandas # Third party library
# Downloaded third party module will be stored in C:\Users\xsbug\AppData\Local\Programs\Python\Python38\Lib\site-packages
while True:
    if os.path.exists("files/temps_today.csv"):
        data = pandas.read_csv("files/temps_today.csv")
        print(data)
        print(type(data)) # <class 'pandas.core.frame.DataFrame'>
        # print(data.mean()) # Get the mean from all columns
        print(data.mean()["st1"]) # Get the mean from column st1
    else:
        print("Files does not exist.")
    time.sleep(10)