# define a function to get the list's mean
def mean(value):
    # if type(value) == dict:
    if isinstance(value, dict):
        the_mean = sum(value.values()) / len(value)
    else:
        the_mean = sum(value) / len(value)
    return the_mean


print(type(mean), type(sum)) # <class 'function'> <class 'builtin_function_or_method'>

print(mean([1, 4, 5]))

studentScore = {'Maria': 83, 'Simon': 75.5, 'Albert': 99}
print(mean(studentScore))



# Function with multiple arguments
def area(x, y):
    return x * y
print(area(4, 5))

# Function arguments with default value
# Note: argument with default value must be the last
def greeting(name, greet = "Hello"):
    return "{}, {}!".format(greet, name)
print(greeting("Alice")) # Use the parameter by default
print(greeting("Bob", "Hi")) # Will overwrite the default parameter
print(greeting("Edwin", greet="Heya")) # Will change the specific parameter
print(greeting(greet="Hey",name="David")) # Same as above

# Function with arbitary numbers of non-keyword arguments
def mean(*args):
    # Note: *args is a tuple type
    return sum(args) / len(args)
print(mean(1, 3, 4, 6))

# Function with arbitary numbers of keyword arguments
def keyword(**kwargs):
    # Note: **kwargs is a dict type
    return kwargs
print(keyword(a=1, b=2, c=3))