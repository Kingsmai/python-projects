section = 10
f = 44
t = 50
for i in range(f, t + 1):
    with open("ce{}-{}".format(section, i), "w") as file:
        content = '''# 

# Hints: 
'''
        file.write(content)