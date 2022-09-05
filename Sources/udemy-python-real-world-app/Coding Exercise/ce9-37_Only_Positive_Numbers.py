# Only Positive Numbers (E)
# Define a function that takes as parameter list of numbers and returns the list containing only the numbers that are greater than 0. For example, I called your function with foo([-5, 3, -1, 101]) it should return [3, 101].

# Hints: If the function parameter is lst you would do [i for i in lst if i > 0 ].
def foo(lst):
    return [i for i in lst if i > 0]