# open up your Python Interpreter in Terminal, and type the code below
import datetime # import module will be explain later
print('The date and time is:', datetime.datetime.now())
# Or you can just locate to this folder in terminal, then input:
# python Demo01Basic.py to run this code

# dir(param) method will return all the thing you can do with a specific type(param)
# You can just type directly in Python Interpreter like this: dir(list)
print(dir(list))
print(dir(int))
print(dir(float))
print(dir(str))
print()

# help(param) method will return the method's usage
# You can just type directly in Python Interpreter like this: help(str.upper)
print(help(str.upper))
print()