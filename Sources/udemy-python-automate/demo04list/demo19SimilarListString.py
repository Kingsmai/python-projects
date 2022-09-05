print(list('Hello'))

name = 'Zophie'
print(name[0])
print(name[1:3])
print(name[-2])
print('Zo' in name)
print('xxx' in name)

for letter in name:
    print(letter)

# String is immutable
name = 'Zophie the cat'
print(name[7])
# name[7] = 'x' # String is immutable

# You need to create a new string to mutate the content
name = 'Zophie a cat'
newName = name[0:7] + 'the' + name[8:12]
print(name)
print(newName)

# Reference notice
spam = 42
cheese = spam
spam = 100
print('spam: ' + str(spam))
print('cheese: ' + str(cheese)) # variable of the cheese wont change (Still 42)

spam = [0, 1, 2, 3, 4, 5] # this will create a reference to [0, 1, 2, 3, 4, 5]
cheese = spam # assign the reference of spam to cheese
cheese[1] = "Hello" # since they refer to same reference, so...
spam[2] = "World"
print('cheese: ' + str(cheese))
print('spam: ' + str(spam)) # because cheese assigned spam's address

def eggs(cheese):
    # The references will be pass in
    cheese.append('Hello')

spam = [1, 2, 3]
eggs(spam)
print(spam)

# to total copy of a list:
import copy
spam = ['A', 'B', 'C', 'D']
cheese = copy.deepcopy(spam)
cheese[1] = 42
print('spam: ' + str(spam))
print('cheese: ' + str(cheese)) # cheese is a brand new list

# Line Continuation
spam = [
    'apples',
    'oranges',
    'bananas',
    'cats'
]
print(spam)

print('Four score and seven' + \
    ' years ago')
print('Four score and seven' + ' years ago')