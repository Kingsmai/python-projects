# Dictionary is a list of collection of many values
# Unlike list, indexes for dictionary are called 'keys' and its associated value is 'value pair'
myCat = {'size': 'fat', 'color': 'gray', 'disposition': 'loud'}
# 'size', 'color', 'dispositon' is key
# 'fat, 'gray', 'loud' is value
print(myCat)

# to get the value:
print(myCat['size'])
print('My cat has ' + myCat['color'] + ' fur.')

# Just like list, key in dictionary can be a integer but don't have to start at zero
myCat = {12345: 'Luggage Combination', 42: 'The Answer'}
print(myCat[12345])

# dictionary is unordered list unlike list
# For example:
print([1, 2, 3] == [3, 2, 1]) # this will return False
# but for dictionary,
eggs = {'name': 'Zophia', 'species': 'cat', 'age': 8}
ham = {'species': 'cat', 'name': 'Zophia', 'age': 8}
print(eggs == ham) # True (even the order of the dictionary is not same)

# if we get a key which is not include in the dictionary list, will thows an exceptions:
# print(eggs['color']) # KeyError: 'color'

# to check the key is included in the dictionary:
print('name' in eggs) # True
print('color' not in eggs) # True

# Get all keys in dictionary:
print(list(eggs.keys()))
print(eggs.keys())
# Get all values in dictionary:
print(list(eggs.values()))
print(eggs.values())
# Get all key / values in dictionary:
print(list(eggs.items()))
print(eggs.items())

# For loops
for k in eggs.keys():
    print(k)

for v in eggs.values():
    print(v)

for k, v in eggs.items():
    print(k, v)

for i in eggs.items():
    print(i)

# to check the value is included in the dictionary:
print('cat' in eggs.values())
print('dog' not in eggs.values())

# Error Preventing:
if 'color' in eggs:
    print(eggs['color'])
else:
    print('color key is not included')

# Another Error Preventing using get() method:
print(eggs.get('age', 0)) # if 'age' is not include in the dictionary, then the default(0) will be returned
print(eggs.get('color', 'black')) # if 'color' is not include in the dictionary, then the default('black') will be returned
# Example:
picnicItems = {'apples': 5, 'cups': 2}
print('I am bringing ' + str(picnicItems.get('napkins', 0)) + ' napkins to the picnic.')

# Set default value
print(eggs)
if 'color' not in eggs:
    eggs['color'] = 'black'
print(eggs)

# Another Set default value using setdefault() method:
eggs = {'name': 'Zophia', 'species': 'cat', 'age': 8} # reset the eggs
print(eggs)
eggs.setdefault('color', 'black')
print(eggs)
eggs.setdefault('color', 'orange') # because color is already exist in the eggs, so it doesn't do anything
print(eggs)
