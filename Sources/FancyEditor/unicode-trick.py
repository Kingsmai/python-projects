lastchar = 120484
firstchar = lastchar - (26 * 26)
upper = 65
lower = 97

with open('Output/Unicode.txt', 'w', encoding='utf-8') as file:
    for idx, i in enumerate(range(upper, upper + (26))):
        # currentChar = f'{chr(i)}, {i}\n'
        currentChar = f'{chr(i)}'
        file.write(currentChar + ' ')
        if (idx + 1) % 26 == 0:
            file.write('\n')

    for idx, i in enumerate(range(lower, lower + (26))):
        # currentChar = f'{chr(i)}, {i}\n'
        currentChar = f'{chr(i)}'
        file.write(currentChar + ' ')
        if (idx + 1) % 26 == 0:
            file.write('\n')

    for idx, i in enumerate(range(firstchar, lastchar)):
        currentChar = f'{chr(i)}, {i}\n'
        # currentChar = f'{chr(i)}'
        file.write(currentChar + ' ')
        if (idx + 1) % 26 == 0:
            file.write('\n')

