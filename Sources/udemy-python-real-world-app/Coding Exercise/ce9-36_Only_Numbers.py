# Only Numbers (E)
# Define a function that takes as a parameter a list that contains both integers and strings and returns the list containing only the integers. For example, if I called your function with foo([99, 'no data', 95, 94, 'no data']) it should return [99, 95, 94].

# Hints: Consider using "if isinstance(i, int)".
def foo(lst):
    return [i for i in lst if isinstance(i, int)]