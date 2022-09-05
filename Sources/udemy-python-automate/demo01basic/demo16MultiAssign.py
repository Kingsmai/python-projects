# Multiple Assignment
cat = ['fat', 'orange', 'loud']
size = cat[0]
color = cat[1]
disposition = cat[2]
# same as
size, color, disposition = cat
print(size)
print(color)
print(disposition)

# also can do list assign
size, color, disposition = 'skinny', 'black', 'quiet'
print(size)
print(color)
print(disposition)

# swapping
a = 'AAA'
b = 'BBB'
a, b = b, a
print(a)
print(b)