# Password Controller (E)
# Define a function that:
# (1) takes a string as parameter
# (2) returns False if the string contains less than 8 characters
# (3) returns True if the string contains 8 or more characters
# If I called your function with foo("mypass") it would return False. If I called it with foo("mylongpassword") it would return True, and so on.

def foo(password):
    return len(password) > 8

# Official Solution:
def foo(password):
    if len(password) >= 8:
        return True
    else:
        return False