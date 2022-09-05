# its a good practice to import module in the first line of script
import sys # Import the sys module
print(sys.builtin_module_names) # print out the Python built-ins modules

import time
print(dir(time)) # print the method of the 'time' module
print(time.sleep) # use help to see how to use the particular method

# To locate the Standard Python Module
print(sys.prefix)
# The in cmd, type: start {the sys.prefix location without{}}
# Then it will open up the window explorer which located the sys.prefix folder
# (in Python 3.8) go to Lib folder and you will see the whole .py file which is the standard Python module
# The location will look like this: C:\Users\xsbug\AppData\Local\Programs\Python\Python38\Lib

# os is a standard Python module
import os

# Let's say we got this situation:
# we write a program connect with server
# this Python script will run 24/7
# it will get a txt file(aka some kind of data) from server, but this file will not be available whole
#   which means sometimes it will be deleted or something else
# So we need to make a conditional weather the file is available
datapath = "files/data.txt"
while True: # run for 24hrs
    if os.path.exists(datapath): # use the "os" module's method
        # if the file exist
        with open(datapath) as file: # open the file as read mode
            print(file.read())
    else:
        print("Files does not exist.")
    time.sleep(60) # Sleep for 60 seconds