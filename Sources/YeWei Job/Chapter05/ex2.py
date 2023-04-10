LINE_COUNT = 5
for i in range(LINE_COUNT):
    line = ''
    for j in range(i + 1):
        line += '*'
    print(line)

for i in range(LINE_COUNT):
    line = ''
    for j in range(LINE_COUNT):
        if j < LINE_COUNT - i - 1:
            line += ' '
        else:
            line += '*'
    print(line)

for i in range(LINE_COUNT):
    line = ''
    for j in range(LINE_COUNT - i - 1):
        line += ' '
    for j in range(i + 1):
        line += '*'
    for j in range(i):
        line += '*'
    print(line)


'''
414
333
252
171
090
'''