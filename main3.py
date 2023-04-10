print(5)
print(int(0b110))
print(int(0o5))
print(int(0x5))

a = [1, 2, 3]
b = [4, 5, 6]
print(a + b)

s = 'abcdefg'
print(s[2:-2])

s1 = '12358'
s2 = '12345'
count = 0
for ch in s1:
    if ch in s2:
        count += 1
print(count)

tmp = 'ab' + 'c' * 2
print(tmp)

mylist = [1, 2, 2, 3, 4, 5]
print(mylist.index(2))

myset = {1, 2, 3, 4, 5}
print(myset)

# v x x v v x v x x x

a = 3
b = -2
a += b
print(a)

a = {1, 2, 3, 4}