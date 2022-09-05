# String Formatting and Uppercase (E)
# Implement a function that gets a person's name (e.g. john) as a parameter and returns a greeting (e.g. Hi John). Note that the first letter of the person's name should always be uppercase.

# Hints: Consider usning name.title() or name.capitalize() to convert the fisrt letter into uppercase.
def foo(name):
    return "Hi %s" % name.title()