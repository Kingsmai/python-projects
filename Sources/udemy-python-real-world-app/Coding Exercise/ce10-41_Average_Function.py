# Average Function (E)
# Define a function that takes an indefinite number of numbers as arguments and returns their average. If I called your function with foo(10, 20, 30, 40) it should return the 25, the average of those numbers.

# Hints: Use def foo(*args).
# To calculate the average, divide sum(args) by len(args).
def foo(*args):
    return sum(args) / len(args)