spam = ['cat', 'bat', 'rat', 'elephant']
print(spam)

print(spam[0])
print(spam[1])
print(spam[2])
print(spam[3])

spam = [['cat', 'bat'], [10, 20, 30, 40, 50]]
print(spam[0])
print(spam[0][1])
print(spam[1][4])

spam = ['cat', 'bat', 'rat', 'elephant']
print(spam[-1])
print(spam[-2])

print('The ' + spam[-1] + 'is afraid of the ' + spam[2] + '.')

# slices
print(spam[1:3]) # start from index 1, and go up to but does not include index 3

# assign new value to list
spam = [10, 20, 30]
spam[1] = 'Hello'
print(spam)

spam[1:3] = ['cat', 'dog', 'mouse']
print(spam)

# slices shortcut
spam = ['cat', 'bat', 'rat', 'elephant']
print(spam[:2]) # start from beginning and go up but not include index 2
print(spam[1:]) # start from index 1 and go up to the last

# delete list item
spam = ['cat', 'bat', 'rat', 'elephant']
del spam[2]
print(spam)

# get list length
print(len([1, 2, 3]))

# concatnation
print([1, 2, 3] + [4, 5, 6])
print([1, 2, 3] * 3)

# convert to list
print(list('Hello'))

# 'in' operator
print('howdy' in ['hello', 'hi', 'howdy', 'heyas'])
print(42 in ['hello', 'hi', 'howdy', 'heyas'])

print('howdy' not in ['hello', 'hi', 'howdy', 'heyas'])
print(42 not in ['hello', 'hi', 'howdy', 'heyas'])