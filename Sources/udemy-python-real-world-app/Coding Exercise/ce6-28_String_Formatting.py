# String Formatting (E)
# Implement a function that gets a person's name as parameter and greets the person with Hi Person. For example, if I called your function with foo("Marry") the function should return Hi Marry .

# Note: If you were to use the f"string" syntax for this exercise you would get an error because f-strings were introduced in Python 3.6 and the Udemy server uses Python 3.5. You might want to use the "%s" syntax instead which works with the older versions of Python. This scenario actually happens often in real life where servers might have an older version of Python so you should be aware and adjust your code accordingly. You can review the string formatting lecture if you forgot the syntax.

def foo(name):
    return "Hi %s" % name