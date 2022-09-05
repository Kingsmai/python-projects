# index
spam = ['hello', ' hi', 'howdy', 'heyas']
print(spam.index('hello')) # return the index value of the param
print(spam.index('heyas'))
try:
    print(spam.index('world')) # if didn't in list, there will be a exception
except ValueError as error:
    print(error)

spam = ['Zophie', 'Pooka', 'Fat-tail', 'Pooka']
print(spam.index('Pooka')) # will return the first time it meet the param

# append
spam = ['cat', 'dog', 'bat']
spam.append('moose') # add to the end of the list
print(spam)

# insert
spam = ['cat', 'dog', 'bat']
spam.insert(1, 'chicken') # insert the value at index 1
print(spam)

#remove
spam = ['cat', 'bat', 'rat', 'elephant']
spam.remove('bat')
print(spam)
try:
    spam.remove('bat') # item didn't inside the list will be a exception
except ValueError as error:
    print(error)

spam = ['cat', 'bat', 'rat', 'cat', 'hat', 'cat']
spam.remove('cat') # will only remove the first one
print(spam)

# 'del' just can remove the item by index
del spam[0]
print(spam)

# sort
spam = [2, 5, 3.14, 1, -7]
spam.sort()
print(spam)

spam = ['ants', 'cats', 'dogs', 'badgers', 'elephants']
spam.sort()
print(spam)
spam.sort(reverse=True)
print(spam)

spam = [1, 2, 3, 'Alice', 'Bob']
# spam.sort() # Python doesn't know how to sort between integer and string

spam = ['Alice', 'Bob', 'ants', 'bats', 'Carol', 'cats']
spam.sort() # it is sort by ASCII-betical order, which means UPPERCASE in front then lowercase
print(spam)

spam = ['a', 'z', 'A', 'Z']
spam.sort()
print(spam)
spam.sort(key=str.lower) # sort in true alphabetical order
print(spam)