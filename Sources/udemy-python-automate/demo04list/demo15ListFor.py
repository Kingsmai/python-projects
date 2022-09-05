print(range(4))

print(list(range(4)))

for i in range(4):
    print(i)

for i in [0, 1, 2, 3]:
    print(i)

print(list(range(0, 100, 2)))

spam = list(range(0, 100, 2))
print(spam)

# for iterate list
supplies = ['pens', 'staplers', 'flame-throwers', 'binders']
for i in range(len(supplies)):
    print('Index ' + str(i) + ' in supplies is: ' + supplies[i] + '.')
