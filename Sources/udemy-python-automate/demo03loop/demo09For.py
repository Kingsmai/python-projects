print('My name is')
for i in range (5):
    print('Jimmy Five Times ' + str(i))
print()

for i in range (12, 16): # 12 to 15
    print('for i loop: ' + str(i))
print()

for i in range (0, 10, 2): # 0 to 9 with 2 step
    print('for i + 2 loop: ' + str(i))
print()

for i in range (5, -1, -1): # 5 to 0 with -1 step
    print('Countdown: ' + str(i))
print()

total = 0
for num in range (101):
    total += num
print("1 + 2 + 3 + ... + 100 = " + str(total))
