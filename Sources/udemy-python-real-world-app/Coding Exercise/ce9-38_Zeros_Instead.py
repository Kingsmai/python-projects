# Zeros Instead (E)
# Define a function that takes as parameter a list that contains both numbers and strings and returns the same list but with zeros instead of strings. For example, I called your function with foo([99, 'no data', 95, 94, 'no data']) it should return [99, 0, 95, 94, 0].

# Hints: You need if and else inside the list comprehension. It goes like this [i if ... else ... for i in lst ].
def foo(lst):
    return [i if not isinstance(i, str) else 0 for i in lst]