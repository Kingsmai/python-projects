# Loop Over Int and Big Colors (E)
# Loop over the colors items and print out the item in every loop only if the item is an integer and it is greater than 50. So, the output of your program would be:

# 54
# 54

# Hints: You can use the and operator to check for two conditionals at the same time.
colors = [11, 34.1, 98.2, 43, 45.1, 54, 54]

for color in colors:
    if isinstance(color, int) and color > 50:
        print(color)